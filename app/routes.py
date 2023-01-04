from app import app
from app import utils
from app import messages
from app.database import Users, Snippets, Source

from flask import render_template, session, request, redirect, flash, abort, url_for, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

import sys
import uuid
import hashlib
from datetime import datetime
from html import escape



@app.after_request
def after_request(response):
  """Ensure responses aren't cached"""

  response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
  response.headers["Expires"] = 0
  response.headers["Pragma"] = "no-cache"
  return response


@app.route("/")
def index():
  try:
    user = Users.objects(user_id=session["user_id"]).first()
    return render_template("index.html", username=user.username), 200
  except (KeyError, AttributeError):
    return render_template("/accounts/login.html"), 401


@app.route("/about")
def about():
  return render_template("/about.html"), 200


@app.route("/faq")
def faq():
  return render_template("/faq.html"), 200


@app.route("/accounts/register", methods=["GET", "POST"])
def register():
  session.clear()

  if request.method == "POST":

    if not request.form.get("username"):
      flash(f"{utils.randomed(messages.response_username())}", "warning")
      return render_template("/accounts/register.html"), 403

    if not request.form.get("password"):
      flash(f"{utils.randomed(messages.response_password())}", "warning")
      return render_template("/accounts/register.html"), 403

    if not request.form.get("confirmation"):
      flash(f"{utils.randomed(messages.response_password())}", "warning")
      return render_template("/accounts/register.html"), 403
    
    if not utils.name_scope(request.form.get("username")):
      flash(f"{utils.randomed(messages.response_username_invalid())}", "warning")
      return render_template("/accounts/register.html"), 403

    if not utils.pass_scope(request.form.get("password"), request.form.get("confirmation")):
      flash(f"{utils.randomed(messages.response_same_pass())}", "warning")
      return render_template("/accounts/register.html"), 403

    for user in Users.objects(username=request.form.get("username")):
      if user.username == request.form.get("username"):
        flash(f"{utils.randomed(messages.response_username_taken(user.username))}", "warning")
        return render_template("/accounts/register.html"), 403

    user_id = str(uuid.uuid4())
    hashed_pass = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256:20000", salt_length=32)
    create_user = Users(username=request.form.get("username"), password=hashed_pass, user_id=user_id)
    create_user.save()
    session["user_id"] = user_id

    flash(f"{utils.randomed(messages.response_welcome('CodeCraft'))}", "success")
    return redirect("/")
  
  else:
    return render_template("/accounts/register.html"), 200


@app.route("/accounts/logout")
def logout():

  session.clear()
  return redirect("/")


@app.route("/accounts/login", methods=["GET", "POST"])
def login():
  session.clear()

  if request.method == "POST":

    if not request.form.get("username"):
      flash(f"{utils.randomed(messages.response_username())}", "warning")
      return render_template("/accounts/login.html"), 403
    
    if not request.form.get("password"):
      flash(f"{utils.randomed(messages.response_password())}", "warning")
      return render_template("/accounts/login.html"), 403
        
    for user in Users.objects(username=request.form.get("username")):
      if not check_password_hash(user.password, request.form.get("password")):
        flash(utils.randomed(messages.response_pass_user()), "warning")
        return render_template("/accounts/login.html"), 403
      else:
        session["user_id"] = user.user_id
        user.update(set__last_online=datetime.utcnow)

        flash(f"{utils.randomed(messages.response_hello(user.username))}", "success")
        return redirect("/")
    
    flash(utils.randomed(messages.response_pass_user()), "warning")
    return render_template("/accounts/login.html"), 403

  else:
    return render_template("/accounts/login.html"), 200


@app.route("/<username>")
def username(username):

  for user in Users.objects(username=username):
    snippets = Snippets.objects(username=username)
    return render_template("/user.html", user=user, snippets=snippets)

  abort(404)


@app.route("/new", methods=["GET", "POST"])
@utils.login_required
def new():

  if request.method == "POST":
    if not request.form.get("code"):
      flash(utils.randomed(messages.response_code()), "danger")
      return redirect("/")
    
    if not utils.data_size(request.form.get("code")):
      size = utils.data_size_in_kb(request.form.get("code"))
      flash(utils.randomed(messages.response_size(size)), "danger")
      return redirect("/")

    if not request.form.get("filename"):
      flash(utils.randomed(messages.response_filename()), "warning")
      return redirect("/")
    
    if len(request.form.get("filename")) > 20:
      flash(utils.randomed(messages.response_filename_len()), "warning")
      return redirect("/")
    
    if request.form.get("description"):
      description = escape(request.form.get("description"))
      if description > 40:
        flash(utils.randomed(messages.response_description_len(), "warning"))
        return redirect("/")
    else:
      description = None

    user = Users.objects(user_id=session["user_id"]).first()
    if user == None:
      return jsonify({"error": "user does not exist"}), 400
    else:
      create_source = Source(
        code=request.form.get("code"),
        filename=request.form.get("filename"),
        hashed=hashlib.sha1(request.form.get("code").encode("utf-8")).hexdigest()
      )
      create_snippet = Snippets(
        snippet_id=str(uuid.uuid4()),
        user_id=user.user_id,
        username=user.username,
        href=utils.generate_path(),
        description=description
      )
      create_snippet.source.append(create_source)
      create_snippet.save()

      flash(utils.randomed(messages.response_snippet_created()), "success")
      return redirect(url_for("snippet", username=user.username, snippet=create_snippet.href))
    
  else:
    abort(404)