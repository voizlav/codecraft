# TODO:

from flask import session, redirect
from functools import wraps
import random
import secrets
import gzip


def login_required(func):
  """ Decorate routes to require login """

  @wraps(func)
  def decorated_function(*args, **kwargs):
    if session.get("user_id") is None:
        return redirect("/accounts/login")
    return func(*args, **kwargs)
  return decorated_function


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


def data_size(source):
  """ Check if the source is in the size scope """
  return len(source.encode("utf-8")) < 2900


def data_size_gzip(source):
  """ Check if the source is in scope while compressed """
  return len(gzip.compress(source.encode("utf-8"))) < 2900


def data_size_in_kb(source):
  """ Return the size of source in KB """
  return round(len(source.encode("utf-8")) / 1024, 2)