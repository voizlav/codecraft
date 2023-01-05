from app.config import USERNAME_LENGTH, PASSWORD_LENGTH, STATUS_LENGTH
from app.config import FILENAME_LENGTH, HREF_LENGTH, DESCRIPTION_LENGTH

from mongoengine import *
from datetime import *



class Source(EmbeddedDocument):
  code          = StringField(required=True)
  date          = DateTimeField(required=True, default=datetime.utcnow)
  filename      = StringField(required=True, max_length=FILENAME_LENGTH)
  version       = IntField(required=True, default=1)
  hashed        = StringField(required=True)


class Snippets(Document):
  snippet_id    = StringField(required=True, primary_key=True)
  user_id       = StringField(required=True)
  username      = StringField(required=True, max_length=USERNAME_LENGTH)
  source        = ListField(EmbeddedDocumentField(Source))
  href          = StringField(required=True, max_length=HREF_LENGTH)
  description   = StringField(reqiured=False, max_length=DESCRIPTION_LENGTH)
  views         = IntField(required=True, default=0)
  deleted       = BooleanField(required=True, default=False)


class Users(Document):
  user_id       = StringField(required=True, primary_key=True)
  username      = StringField(required=True, max_length=USERNAME_LENGTH)
  email         = EmailField(required=False, default=None)
  password      = StringField(required=True, max_length=PASSWORD_LENGTH)
  deleted       = BooleanField(required=True, default=False)
  register_date = DateTimeField(required=True, default=datetime.utcnow)
  last_online   = DateTimeField(default=datetime.utcnow)
  premium       = BooleanField(required=True, default=False)
  status        = StringField(required=True, default=None, max_length=STATUS_LENGTH)