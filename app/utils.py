from app.config import RESERVED_USERNAMES, USERNAME_LENGTH, PASSWORD_LENGTH, DATA_SIZE

from flask import session, redirect
from functools import wraps

import random
import secrets
import gzip
import re


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
    return password == comfirm and len(password) > 0 and len(password) < PASSWORD_LENGTH


def name_scope(username):
    """ Check username input """

    try:
      return str(username).lower() not in RESERVED_USERNAMES and len(username) <= USERNAME_LENGTH and len(username) > 0 and str(username).isalnum()     
    except (AttributeError, TypeError):
      return False


def generate_path():
  """ Generate a random hexadecimal string """
  return secrets.token_hex(6)[:6]


def data_size(source):
  """ Check if the source is in the size scope """
  return len(source.encode("utf-8")) < DATA_SIZE


def data_size_gzip(source):
  """ Check if the source is in scope while compressed """
  return len(gzip.compress(source.encode("utf-8"))) < DATA_SIZE


def data_size_in_kb(source):
  """ Return the size of source in KB """
  return round(len(source.encode("utf-8")) / 1024, 2)


def filename_scope(filename):
  """ Check if the file name is valid """
  return bool(re.match("^(?!(?:\.|-))(?:(?:[A-z0-9]|(?<!(?:\.|-|_))(?:\.|-|_{1,3}))+)(?<!(?:\.|-))$", filename))