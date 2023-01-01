from mongoengine import *
from datetime import *


class Snippets(Document):
  snippet_id    = StringField(required=True, primary_key=True)
  user_id       = StringField(required=True)
  username      = StringField(required=True, max_length=20)
  source        = ListField(EmbeddedDocumentField(Source))
  href          = StringField(required=True, max_length=10)
  description   = StringField(reqiured=False)
  views         = IntField(required=True, default=0)
  deleted       = BooleanField(required=True, default=False)


class Users(Document):
  user_id       = StringField(required=True, primary_key=True)
  username      = StringField(required=True, max_length=20)
  email         = EmailField(required=False, default=None)
  password      = StringField(required=True, max_length=120)
  deleted       = BooleanField(required=True, default=False)
  register_date = DateTimeField(required=True, default=datetime.utcnow)
  last_online   = DateTimeField(default=datetime.utcnow)
  premium       = BooleanField(required=True, default=False)