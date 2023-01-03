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
    "Provide a username to move forward.",
    "Enter a username to proceed."
    "Please input a username to continue."
    "Submit a username to go on."
    "A username is required to continue."
    "Enter a username to keep going."
    "Please enter a username to continue the process."
    "A username is necessary to proceed."
    "Provide a username to continue the task."
    "Please submit a username to continue the journey."
  ]


def response_password():
  return [
    "Password required.",
    "Password must be submitted.",
    "Need to enter password.",
    "Password must be entered.",
    "Password is required.",
    "A password must be provided.",
    "Please enter a password.",
    "A password is needed.",
    "You must provide a password.",
    "Password input is required."
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


def response_description_len():
  return [
    "Your description is too long. Please keep it brief.",
    "The description exceeds the maximum allowed length.",
    "Please reduce the length of your description.",
    "Description is too lengthy. Please shorten it.",
    "The description is too long. Please revise it.",
    "The description exceeds the maximum character limit.",
    "Your description is too lengthy. Please trim it down.",
    "The description is too long. Please make it shorter.",
    "Please shorten the description as it exceeds the limit."
  ]


def response_filename_len():
  return [
    "This file name is way too long!",
    "Geez, who came up with this file name? It's never ending!",
    "The file name is way too long, it won't work.",
    "The file name is way too long.",
    "This file name is a mouthful.",
    "The file name is seriously dragging on.",
    "This file name is ridiculous.",
    "The file name is almost as long as my attention span.",
    "This file name is longer than my arm.",
    "The file name is more complicated than a Rubik's cube.",
    "This file name is a novel in itself.",
    "The file name is a never-ending story.",
    "This file name is like a marathon."
  ]


def response_snippet_created():
  return []


def response_snippet_edit():
  return []


def response_pass_user():
  return []


def response_hello(username):
  return [
    f"Welcome back {username}, we've been waiting for you to grace us with your coding skills.",
    f"{username}, it's great to see you back on the app! We missed your contributions to the community.",
    f"{username}, your absence has been felt, but now you're back and ready to tackle some code!",
    f"{username}, it's always a pleasure to have you back on the app. Your coding skills are unmatched.",
    f"Welcome back {username}, we've been staring at a blank screen without you.",
    f"{username}, it's good to see you back and ready to tackle some code challenges.",
    f"{username}, we've been missing your brilliant coding solutions. Welcome back to the app!",
    f"Welcome back {username}, the app has been a little dull without your coding genius.",
    f"{username}, it's always a pleasure to have you back on the app. Your coding skills are unparalleled.",
    f"Welcome back {username}, we've been counting the minutes until your return.",
    f"Ahoy, matey! Welcome back {username}!",
    f"Greetings and salutations, {username}! We've missed you!",
    f"Yo, {username}! Good to have you back in the saddle!",
    f"Eureka! {username} has returned! Welcome back, dear friend!",
    f"Bonjour, mon ami! Welcome back, {username}!",
    f"Hark! {username} hath returned! Welcome back, adventurer!",
    f"Ah, {username}! We've been waiting for you. Welcome back, buddy!",
    f"Salutations, {username}! It's good to see you again.",
    f"Tada! {username} is back in the house! Welcome home, pal!",
    f"Hello there, {username}! Welcome back to the land of the living!",
    f"Ahoy there, {username}! It's good to have you back on board the ship of mediocrity.",
    f"Greetings, {username}! We've been holding a spot for you in the awkward silence corner."
  ]



def response_login():
  return [
    "Don't have a login?",
    "No account yet?",
    "Haven't made an account?",
    "Not signed up?",
    "No login set up?",
    "Haven't created a login yet?",
    "Not registered yet?",
    "Don't have a profile?",
    "Haven't gotten around to making an account?",
    "Not a member yet?",
    "Haven't set up an account?",
    "No login information?",
    "Not part of the club yet?",
    "Haven't gotten an account?",
    "No account yet? Time to fix that!",
    "Haven't joined the party yet? You're missing out!",
    "No profile to call your own? Let's change that.",
    "Not part of the club yet? It's never too late to register.",
    "No account to your name? Time to rectify that situation.",
    "Haven't created a profile yet? What are you waiting for?",
    "Not a member yet? Don't be left out in the cold.",
    "No account to speak of? Time to rectify that.",
    "Haven't made a profile yet? It's time to get on board.",
    "No account under your name? Time to change that."
  ]


def response_register():
  return [
    "Do you have an account?",
    "Do you already have an account?",
    "You have an account, right?",
    "Already set up an account?",
    "Have you made an account yet?",
    "Are you registered with us?",
    "Do you have a login?",
    "Have you created an account with us?",
    "Do you have a username and password?",
    "Are you a member with us?",
    "Do you have a profile set up?",
    "Have you signed up yet?",
    "Do you have a user account?",
    "Do you have an online account?",
    "Are you registered on this site?",
    "Oh, you have an account? I'm shocked.",
    "Do you have a secret account that I don't know about?"
  ]

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
