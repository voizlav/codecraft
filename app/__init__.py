import os

from flask import Flask
from flask_session import Session
from dotenv import load_dotenv
from mongoengine import connect
from app.utils import data_size, randomed_greet


# Load the .env file and any exported environment variables
load_dotenv(override=True)

# Initialize the app and apply the provided configuration values
app = Flask(__name__)
app.config.update(
  SESSION_PERMANENT = False,
  SESSION_TYPE      = "filesystem",
  DEBUG             = os.getenv("DEBUG"),
  FLASK_DEBUG       = os.getenv("FLASK_DEBUG"),
  DATABASE_URI      = os.getenv("DATABASE_URI"),
  DATABASE_NAME     = os.getenv("DATABASE_NAME")
)
Session(app)

# Ensure that the DATABASE_URI and DATABASE_NAME environment variables have been set
if not os.getenv("DATABASE_URI"):
  raise RuntimeError("Database URI is missing from the configuration")

if not os.getenv("DATABASE_NAME"):
  raise RuntimeError("Database name is missing from the configuration")

# Establish a connection to the MongoDB database using the mongoengine library
connect(app.config["DATABASE_NAME"], app.config["DATABASE_URI"])

# TODO: