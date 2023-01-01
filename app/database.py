from mongoengine import *
from datetime import *


class Users(Document):
  user_id       = StringField(required=True, primary_key=True)
  username      = StringField(required=True, max_length=20)
  email         = EmailField(required=False, default=None)
  password      = StringField(required=True, max_length=120)
  deleted       = BooleanField(required=True, default=False)
  register_date = DateTimeField(required=True, default=datetime.utcnow)
  last_online   = DateTimeField(default=datetime.utcnow)
  premium       = BooleanField(required=True, default=False)