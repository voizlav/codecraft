from app import app
from flask import render_template, session
from database import Users, Snippets, Source


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
    return render_template(
      "index.html",
      username=user.username,
      filename_too_long=response_filename_len())
  
  except (KeyError, AttributeError):
    return render_template(
      "accounts/login.html",
      questions=response_login())