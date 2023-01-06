from app import app
from app import utils
from app import messages
from app.database import Users, Snippets, Source
from app.config import FILENAME_LENGTH, DESCRIPTION_LENGTH

from flask import Response, render_template, session, request, redirect, flash, abort, url_for, jsonify, send_file
from werkzeug.security import check_password_hash, generate_password_hash

import io
import json
import base64
import qrcode
import uuid
import hashlib
import gzip
from datetime import datetime



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
    return render_template("index.jinja2", username=user.username), 200
  except (KeyError, AttributeError):
    return render_template("/accounts/login.jinja2"), 401


@app.route("/about")
def about():
  return render_template("/about.jinja2"), 200


@app.route("/faq")
def faq():
  return render_template("/faq.jinja2"), 200


@app.route("/accounts/register", methods=["GET", "POST"])
def register():
  session.clear()

  if request.method == "POST":

    if not request.form.get("username"):
      flash(f"{utils.randomed(messages.response_username())}", "warning")
      return render_template("/accounts/register.jinja2"), 403

    if not request.form.get("password"):
      flash(f"{utils.randomed(messages.response_password())}", "warning")
      return render_template("/accounts/register.jinja2"), 403

    if not request.form.get("confirmation"):
      flash(f"{utils.randomed(messages.response_password())}", "warning")
      return render_template("/accounts/register.jinja2"), 403
    
    if not utils.name_scope(request.form.get("username")):
      flash(f"{utils.randomed(messages.response_username_invalid())}", "warning")
      return render_template("/accounts/register.jinja2"), 403

    if not utils.pass_scope(request.form.get("password"), request.form.get("confirmation")):
      flash(f"{utils.randomed(messages.response_same_pass())}", "warning")
      return render_template("/accounts/register.jinja2"), 403

    for user in Users.objects(username=request.form.get("username")):
      if user.username == request.form.get("username"):
        flash(f"{utils.randomed(messages.response_username_taken(user.username))}", "warning")
        return render_template("/accounts/register.jinja2"), 403

    user_id = str(uuid.uuid4())
    hashed_pass = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256:20000", salt_length=32)
    user_status = utils.randomed(messages.response_set_default_status())
    create_user = Users(username=request.form.get("username"), password=hashed_pass, user_id=user_id, status=user_status)
    create_user.save()
    session["user_id"] = user_id

    flash(f"{utils.randomed(messages.response_welcome('CodeCraft'))}", "success")
    return redirect("/")
  
  else:
    return render_template("/accounts/register.jinja2"), 200


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
      return render_template("/accounts/login.jinja2"), 403
    
    if not request.form.get("password"):
      flash(f"{utils.randomed(messages.response_password())}", "warning")
      return render_template("/accounts/login.jinja2"), 403
        
    for user in Users.objects(username=request.form.get("username")):
      if not check_password_hash(user.password, request.form.get("password")):
        flash(utils.randomed(messages.response_pass_user()), "warning")
        return render_template("/accounts/login.jinja2"), 403
      else:
        session["user_id"] = user.user_id
        user.update(set__last_online=datetime.utcnow)

        flash(f"{utils.randomed(messages.response_hello(user.username))}", "success")
        return redirect("/")
    
    flash(utils.randomed(messages.response_pass_user()), "warning")
    return render_template("/accounts/login.jinja2"), 403

  else:
    return render_template("/accounts/login.jinja2"), 200


@app.route("/<username>")
def username(username):

  for user in Users.objects(username=username):
    snippets = Snippets.objects(username=username)
    return render_template("/username/profile.jinja2", user=user, snippets=snippets)

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
      flash(utils.randomed(messages.response_filename_blank()), "warning")
      return redirect("/")
    
    if len(request.form.get("filename")) > FILENAME_LENGTH:
      flash(utils.randomed(messages.response_filename_len()), "warning")
      return redirect("/")
    
    if not utils.filename_scope(request.form.get("filename")):
      flash(utils.randomed(messages.response_filename_invalid()), "warning")
      return redirect("/")
    
    if request.form.get("description"):
      description = request.form.get("description")
      if len(description) > DESCRIPTION_LENGTH:
        flash(utils.randomed(messages.response_description_len()), "warning")
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


@app.route("/<username>/<snippet>")
def snippet(username, snippet):

  for snippet in Snippets.objects(username=username, href=snippet):
    user = Users.objects(username=username).first()
    snippet.views += 1
    snippet.save()

    return render_template("/username/snippet.jinja2", username=username, snippet=snippet, sourcecode=snippet.source[-1], user_id=user.user_id)

  abort(404)


@app.route("/<username>/<snippet>/<version>/raw")
def source(username, snippet, version):

  for snippet in Snippets.objects(username=username, href=snippet):
    for source in snippet.source:
      try:
        if int(version) == source.version:
          return Response(source.code, mimetype="text/plain")
      except (ValueError, IndexError):
        abort(404)
  
  abort(404)


@app.route("/<username>/<snippet>/<version>/edit", methods=["GET", "POST"])
@utils.login_required
def edit(username, snippet, version):
  
  # TODO: need utils tool for version input check !

  if request.method == "POST":

    if not request.form.get("code"):
      flash(utils.randomed(messages.response_code()), "danger")
      return redirect(url_for("snippet", username=username, snippet=snippet))

    if not utils.data_size(request.form.get("code")):
      if not utils.data_size_gzip(request.form.get("code")):
        flash(utils.randomed(messages.response_size(utils.data_size_in_kb(request.form.get("code")))), "danger")
        return redirect(url_for("snippet", username=username, snippet=snippet))
    
    if not request.form.get("filename"):
      flash(utils.randomed(messages.response_filename_blank()), "danger")
      return redirect(url_for("snippet", username=username, snippet=snippet))
    
    if len(request.form.get("filename")) > FILENAME_LENGTH:
      flash(utils.randomed(messages.response_filename_len()), "warning")
      return redirect(url_for("snippet", username=username, snippet=snippet))

    if not utils.filename_scope(request.form.get("filename")):
      flash(utils.randomed(messages.response_filename_invalid()), "warning")
      return redirect(url_for("snippet", username=username, snippet=snippet))
    
    user = Users.objects(username=username, user_id=session["user_id"]).first()
    if user == None:
      return jsonify({"error": "Sorry, you are not authorized to access this resource."}), 401
    else:
      edit_snippet = Snippets.objects(href=snippet).first()
      new_source = Source(
        code=request.form.get("code"),
        filename=request.form.get("filename"),
        hashed=hashlib.sha1(request.form.get("code").encode("utf-8")).hexdigest(),
        version=edit_snippet.source[-1].version+1
        )
      edit_snippet.source.append(new_source)
      edit_snippet.save()

      flash(utils.randomed(messages.response_snippet_edit()), "success")
      return redirect(url_for("snippet", username=username, snippet=snippet))
  
  else:
    user = Users.objects(username=username, user_id=session["user_id"]).first()
    if user == None:
      abort(404)
    else:
      get_snippet = Snippets.objects(href=snippet).first()
      try:
        get_snippet.source[int(version)-1].code
        return render_template("/username/edit.jinja2", snippet=get_snippet, version=int(version))
      except (ValueError, IndexError):
        abort(404)


@app.route("/<username>/<snippet>/<version>")
def version(username, snippet, version):

  for snippet in Snippets.objects(username=username, href=snippet):
    for source in snippet.source:
      try:
        if int(version) == source.version:
          user = Users.objects(username=username).first()
          snippet.views += 1
          snippet.save()
          return render_template("/username/snippet.jinja2", snippet=snippet, sourcecode=source, user_id=user.user_id) 
      except ValueError:
        return abort(404)
      
  abort(404)


@app.route("/<username>/source/<hash>.png")
def img(username, hash):

  for snippet in Snippets.objects(username=username):
    for source in snippet.source:
      if hash == source.hashed:
        buffer = io.BytesIO()
        if utils.data_size(source.code):
          img = qrcode.make(source.code, error_correction=qrcode.ERROR_CORRECT_L)
          img.save(buffer)
        else: 
          source = source.code
          source = gzip.compress(source.encode())
          img = qrcode.make(source, error_correction=qrcode.ERROR_CORRECT_L)
          img.save(buffer)
        
        buffer.seek(0)
        return send_file(buffer, mimetype="image/png")
  else:
    abort(404)