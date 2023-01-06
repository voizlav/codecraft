import os


DEBUG              = os.getenv("DEBUG")
FLASK_DEBUG        = os.getenv("FLASK_DEBUG")
FLASK_RUN_PORT     = 5000

SESSION_PERMANENT  = False
SESSION_TYPE       = "filesystem"

DATABASE_URI       = os.getenv("DATABASE_URI")
DATABASE_NAME      = os.getenv("DATABASE_NAME")

DATA_SIZE          = 2900
HREF_LENGTH        = 10
DESCRIPTION_LENGTH = 120
FILENAME_LENGTH    = 20
STATUS_LENGTH      = 30
PASSWORD_LENGTH    = 120
USERNAME_LENGTH    = 20

RESERVED_USERNAMES = [
  "admin",
  "root",
  "administrator",
  "webmaster",
  "support",
  "info",
  "contact",
  "help",
  "sysadmin",
  "security",
  "moderator",
  "accounts",
  "new",
  "faq",
  "about"
]