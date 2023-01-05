import os
import json
import base64
import hashlib

from flask import Flask
from flask_session import Session
from dotenv import load_dotenv
from mongoengine import connect

from utils import data_size, randomed
from app import messages

from config import SESSION_PERMANENT, SESSION_TYPE
from config import FLASK_DEBUG, DEBUG
from config import DATABASE_URI, DATABASE_NAME


# Load the .env file and any exported environment variables
load_dotenv(override=True)

# Initialize the app and apply the provided configuration values
app = Flask(__name__)
app.config.update(
  SESSION_PERMANENT = SESSION_PERMANENT,
  SESSION_TYPE      = SESSION_TYPE,
  DEBUG             = DEBUG,
  FLASK_DEBUG       = FLASK_DEBUG,
  DATABASE_URI      = DATABASE_URI,
  DATABASE_NAME     = DATABASE_NAME
)
Session(app)

# Ensure that the DATABASE_URI and DATABASE_NAME environment variables have been set
if not os.getenv("DATABASE_URI"):
  raise RuntimeError("Database URI is missing from the configuration")

if not os.getenv("DATABASE_NAME"):
  raise RuntimeError("Database name is missing from the configuration")

# Establish a connection to the MongoDB database using the mongoengine library
connect(app.config["DATABASE_NAME"], host=app.config["DATABASE_URI"])

# Customize Jinja filters for the app's template engine
app.jinja_env.filters["hash"] = lambda source: hashlib.sha1(source.encode("utf-8")).hexdigest()
app.jinja_env.filters["encode"] = lambda source: base64.urlsafe_b64encode(json.dumps(source).encode("utf-8")).decode("utf-8")
app.jinja_env.filters["size"] = lambda source: round(len(source.encode("utf-8")) / 1024, 2)
app.jinja_env.filters["gzipped"] = lambda source: data_size(source)
app.jinja_env.filters["randomed"] = randomed

# Customize Jinja globals for the app's template engine
app.jinja_env.globals["response_login"] = messages.response_login()
app.jinja_env.globals["response_register"] = messages.response_register()
app.jinja_env.globals["not_found_paragraph"] = messages.response_not_found_paragraph()
app.jinja_env.globals["not_found_header"] = messages.response_not_found_header()
app.jinja_env.globals["filename_too_long"] = messages.response_filename_len()
app.jinja_env.globals["description_too_long"] = messages.response_description_len()


from app import routes, error, database, utils