from app import app
import uuid
from flask import render_template, session, request, redirect, flash, abort
from werkzeug.security import check_password_hash, generate_password_hash
from app.database import Users, Snippets, Source

from app import utils
from app import messages



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
    return render_template("accounts/login.html"), 401


@app.route("/about")
def about():
  return render_template("about.html"), 200


@app.route("/faq")
def faq():
  return render_template("faq.html"), 200


@app.route("/accounts/register", methods=["GET", "POST"])
def register():
  session.clear()

  if request.method == "POST":

    if not request.form.get("username"):
      flash(f"{utils.randomed(messages.response_username())}", "warning")
      return render_template("/accounts/register.html"), 403

    elif not request.form.get("password"):
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
    return render_template("index.html", username=create_user.username), 200
  
  else:
    return render_template("/accounts/register.html"), 200