# TODO:


def response_welcome(app):
  return [
    f"Congratulations, you are now a member of {app}!",
    f"Welcome to {app}! Your registration was successful.",
    f"Thank you for registering with {app}. Your account has been created successfully.",
    f"You're all set! Your registration on {app} was successful.",
    f"Great news! Your registration on {app} was successful. Welcome aboard!",
    f"Welcome to {app}! Your registration was a success.",
    f"Your registration on {app} was successful. Welcome to the community!",
    f"Congratulations on successfully registering with {app}! Welcome.",
    f"You have successfully registered for {app}. Welcome to the team!",
    f"Your registration with {app} was successful. We're glad to have you onboard. Welcome!",
    "Congratulations, your registration was successful!",
    "Welcome to our community! Your registration was successful.",
    "Your account has been created successfully. Thank you for registering.",
    "You are now a member of our platform. Your registration was successful.",
    "Your registration was successful. We're glad to have you on board.",
    "Welcome aboard! Your registration was successful.",
    "Your registration process is complete. Thank you for joining us.",
    "Congratulations on your successful registration. Welcome to the team!",
    "Your registration was successful. We look forward to your participation.",
    "Welcome to the family! Your registration was successful."
  ]


def response_username_taken(username):
  return [
    f"Sorry, but the username '{username}' is already taken. Please try a different one.",
    f"I'm sorry, but the username '{username}' is not available. Please choose a different one.",
    f"Unfortunately, the username '{username}' is not available. Please select a different one.",
    f"The username '{username}' is already in use. Please choose a different one.",
    f"I'm afraid the username '{username}' is not available. Please try another one.",
    f"Unfortunately, the username '{username}' has already been taken. Please select a different one.",
    f"The username '{username}' is unavailable. Please choose a different one.",
    f"I'm sorry, but the username '{username}' is already in use. Please try a different one.",
    f"The username '{username}' is not available. Please select a different one.",
    f"Sorry, but the username '{username}' has already been taken. Please choose a different one.",
    "Sorry, that username is already taken.",
    "The username you have chosen is not available.",
    "The username you entered is already in use.",
    "We're sorry, but the username you have selected is unavailable.",
    "Unfortunately, the username you entered is taken.",
    "The username you have chosen is already registered.",
    "We're sorry, but that username is not available.",
    "The username you entered has already been taken by another user.",
    "I'm sorry, but the username you selected is not available.",
    "Unfortunately, the username you have chosen is already in use by another user."
  ]


def response_username_invalid():
  return [
    "You must enter a valid username to register.",
    "Invalid username. Please enter a valid username to register.",
    "A valid username is required to complete registration.",
    "The username you entered is not valid. Please enter a different username to register.",
    "Please provide a valid username to complete registration.",
    "The username you entered is not valid. Please enter a different username.",
    "A valid username is required to create an account.",
    "Invalid username. Please enter a valid username to create an account.",
    "You must enter a valid username to create an account.",
    "The username you entered is not valid. Please enter a different username to create an account."
  ]


def response_username():
  return [
    "Please enter a username to continue registration.",
    "Username is required for registration.",
    "A username is necessary to create an account.",
    "You must choose a username to complete registration.",
    "A valid username is required to register.",
    "Please enter a unique username to create your account.",
    "Username field must be filled in to proceed with registration.",
    "You need to select a username before you can complete the registration process.",
    "A username is required in order to create your account.",
    "Please provide a username to complete your registration."
  ]


def response_password():
  return [
    "You must enter a password to create an account.",
    "A password is required to complete registration.",
    "Please provide a password to sign up.",
    "You need to choose a password to finish registering.",
    "A password must be entered to complete the registration process.",
    "A password is mandatory for creating an account.",
    "Please create a password in order to register.",
    "You must select a password to complete the registration form.",
    "A password is required to create your account.",
    "Please enter a password to complete the sign up process."
  ]


def response_same_pass():
  return [
    "Please enter the same password in both fields.",
    "The passwords you entered do not match.",
    "You must enter the same password twice to confirm it.",
    "The password confirmation does not match the password.",
    "Please re-enter your password to confirm it.",
    "Your passwords must match in order to complete registration.",
    "Please ensure that your passwords are the same.",
    "The password and confirmation must be the same.",
    "The two password fields must contain the same value.",
    "You must enter the same password in both the password and confirm password fields."
  ]


def response_code():
  return []


def response_size(size):
  return []


def response_filename():
  return []


def response_filename_len():
  return []


def response_snippet_created():
  return []


def response_snippet_edit():
  return []


def response_pass_user():
  return []


def response_hello(username):
  return []



def response_login():
  return []


def response_register():
  return []


def response_delete_snippet():
  return []


def response_delete_title():
  return []


def response_not_found_header():
  return [
    "This page is not available.",
    "Sorry, we can't access this page.",
    "This page is not accessible.",
    "We're sorry, this page cannot be displayed.",
    "This page is currently unavailable.",
    "Sorry, but this page is not available.",
    "We apologize, but this page cannot be accessed.",
    "Sorry, this page is not found.",
    "We're sorry, but this page is not available at this time.",
    "Sorry, but we cannot access this page."
  ]


def response_not_found_paragraph():
  return [
    "It seems the link you clicked on may be faulty or the page may have been removed.",
    "There may be an issue with the link you tried to access, or the page may no longer exist.",
    "It's possible the link you followed is incorrect or the page has been removed.",
    "There seems to be a problem with the link you tried to access, or the page may no longer be available.",
    "The link you clicked on may have been broken or the page may have been removed from the website.",
    "It's possible the link you followed is no longer valid or the page has been taken down.",
    "There seems to be an issue with the link you attempted to access, or the page may have been removed from the site.",
    "The link you followed may not be functioning properly, or the page may have been removed.",
    "It's possible the link you tried to access is invalid or the page has been removed from the website.",
    "There may be a problem with the link you clicked on, or the page may no longer be available."
  ]
