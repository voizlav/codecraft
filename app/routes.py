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