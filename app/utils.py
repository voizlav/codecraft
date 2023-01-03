# TODO:

import random
import secrets


def randomed(message):
  """ Choose a random message """
  return random.choice(message)


def pass_scope(password, comfirm):
    """ Check password input """
    return password == comfirm and len(password) > 0 and len(password) < 64


def name_scope(username):
    """ Check username input """
    RESERVED = ["accounts", "new", "faq", "about"]

    try:
      return str(username).lower() not in RESERVED and len(username) <= 20 and len(username) > 0 and str(username).isalnum()     
    except (AttributeError, TypeError):
      return False


def generate_path():
  """ Generate a random hexadecimal string """
  return secrets.token_hex(6)[:6]


def login_required(func):
  """ Decorate routes to require login """

  @wraps(func)
  def decorated_function(*args, **kwargs):
    if session.get("user_id") is None:
        return redirect("/accounts/login")

    return func(*args, **kwargs)

  return decorated_function