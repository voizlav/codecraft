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
    "Enter a username to proceed.",
    "Please input a username to continue.",
    "Submit a username to go on.",
    "A username is required to continue."
    "Enter a username to keep going.",
    "Please enter a username to continue the process.",
    "A username is necessary to proceed.",
    "Provide a username to continue the task.",
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
  return [
    "It is not possible to submit an empty source code.",
    "The source code cannot be left blank.",
    "A source code cannot be submitted without any content.",
    "It is required to have content in the source code.",
    "An empty source code is not allowed.",
    "The source code must contain something.",
    "Looks like the source code is completely blank.",
    "There's not a single line of code in the source.",
    "The source code file is empty as a ghost town.",
    "I think someone forgot to add any code to the source.",
    "I don't see anything in the source code.",
    "It's like the source code was never touched.",
    "I'm not seeing any code in the source.",
    "The source code looks like it's been erased.",
    "I don't think there's anything in the source code.",
    "The source code is as empty as a desert."
  ]


def response_size(size):
  return [
    f"This source code is way too big at {size} KB - we need to trim it down.",
    f"Whoa, {size} KB for code snippet? That's insane.",
    f"I can't even begin to wrap my head around a source code this massive at {size} KB.",
    f"Looks like we've got a giant source code on our hands at {size} KB.",
    f"I don't think my server can handle this {size} KB source code.",
    f"I'm not sure how we're going to manage this huge source code of {size} KB.",
    f"Geez, {size} KB for source code? That's a lot to take in.",
    f"I don't know if I'm ready for this massive {size} KB source code.",
    f"This source code is seriously huge at {size} KB - where do we even begin?",
    f"I think we might have bitten off more than we can handle with this {size} KB source code.",
    f"Haha, I guess I went a little snippet-crazy at {size} KB!",
    "Whoa, this source code is way too big for my liking.",
    "I feel like I'm in the Matrix trying to navigate through this giant codebase.",
    "I can't even wrap my head around this source code, it's so massive.",
    "I don't have the patience to sift through all of this lengthy source code.",
    "This source code is like a never-ending novel, it's so long.",
    "I can't believe how massive this source code is. It's overwhelming.",
    "I think I need a break after looking at this huge source code.",
    "I'm starting to feel like I'll never reach the end of this giant source code.",
    "I don't know if I'm up for tackling such a large source code.",
    "I feel like I'm drowning in this massive source code."
  ]


def response_filename_blank():
  return [
    "You cannot leave the filename blank.",
    "A filename must be entered.",
    "The filename field cannot be left blank.",
    "You must provide a filename.",
    "Please enter a filename.",
    "It is required to enter a filename.",
    "An empty filename is not allowed.",
    "The filename cannot be left empty.",
    "A non-empty filename is required.",
    "You must enter a valid filename.",
    "Hey, you didn't give a name for the file.",
    "What should I call this file? You didn't specify a name.",
    "Oops, looks like you forgot to name the file.",
    "I can't save it if you don't tell me what to name it.",
    "A file needs a name, and you didn't provide one.",
    "Don't forget to name the file before saving it.",
    "You need to give this file a name before proceeding.",
    "Uh oh, you didn't specify a file name.",
    "You can't just leave the file name blank.",
    "I need a name for this file - can you give me one?"
  ]


def response_filename_invalid():
  return [
    "Invalid file name.",
    "File name is incorrect",
    "File name does not meet the required standards.",
    "Unacceptable file name.",
    "File name does not follow the proper format.",
    "Invalid characters in file name.",
    "File name is not in the correct format.",
    "Incorrect file name syntax.",
    "File name does not comply with guidelines.",
    "File name fails to meet the necessary criteria.",
    "This file is like a bad joke - not valid.",
    "I'm sorry, but this file is too sassy for its own good.",
    "I think someone was feeling a bit lazy when they named this file.",
    "This file is like a prank gone wrong - not valid."
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


def response_snippet_created():
  return [
    "Looks like we're ready to rock and roll with this new code!",
    "Code complete, party time!",
    "Congratulations, we've brought a new life into the world: source code!",
    "This code is a masterpiece, a work of art.",
    "Looks like we've created the next big thing in software development.",
    "Code creation success: let's pop some champagne!",
    "We've created a code Frankenstein, and it's alive!",
    "Code complete, and it's a thing of beauty.",
    "We did it! A perfectly functioning code snippet has been conjured into existence.",
    "The code snippet has been created and all is right in the world once again.",
    "Another code snippet down, only a million more to go. #codinglife",
    "Look out world, we've got another code snippet on the loose!",
    "Another code snippet has been added to our arsenal of awesome code.",
    "Code snippet creation success! Time for a well-deserved victory dance.",
    "We've created another code snippet and it's a thing of beauty. #codingmagic"
  ]


def response_snippet_edit():
  return [
    "Code fixin' done right!",
    "We're now running on the latest and greatest codebase!",
    "Source code upgrade complete, system running smoothly!",
    "It's a code party in here!",
    "Code update successful, time to celebrate with some bug-free programming!",
    "Source code update complete, bring on the new features!",
    "Code update success! Time to kick back and let the server do the work.",
    "Code update complete, system running like a well-oiled machine!",
    "The code gods are pleased with your updates and have bestowed upon you their blessing.",
    "You have successfully avoided the code apocalypse and saved us all from certain doom.",
    "Your code updates have brought peace to the world and cured world hunger."
  ]


def response_pass_user():
  return [
    "Uh oh! It looks like your login information is not accurate.",
    "Sorry, but the login details you provided are incorrect.",
    "I'm afraid your username and password are not matching our records.",
    "Unfortunately, the login information you entered is incorrect.",
    "It appears that your login credentials are not correct.",
    "Oof, it seems like the login information you provided is incorrect.",
    "I'm sorry, but your login details do not match our records.",
    "Oh no, it looks like your login information is incorrect.",
    "Sorry, but the login credentials you entered are not correct.",
    "I'm afraid the login details you provided are not accurate."
  ]


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
  return [
    "Are you sure you want to delete the snippet?",
    "You sure you wanna delete that snippet?",
    "Are you positive you want to get rid of the snippet?",
    "Do you really want to erase the snippet?",
    "You want to delete that snippet for sure?",
    "You want to delete the snippet, right?",
    "Are you certain you want to delete the snippet?",
    "You sure you want to delete that snippet, right?",
    "You definitely want to delete the snippet?",
    "Are you completely sure you want to delete the snippet?",
    "You want to delete the snippet without a doubt?",
    "You really want to delete the snippet, right?",
    "Are you sure you want to get rid of the snippet?",
    "You definitely want to delete the snippet, right?",
    "You want to delete the snippet for sure, right?",
    "Are you certain you want to erase the snippet?",
    "You sure you wanna nuke this thing?"
  ]


def response_delete_title():
  return [
    "Get rid of that little piece of code",
    "Wipe out that code segment",
    "Trash that bit of code",
    "Get rid of that code fragment",
    "Eliminate that code snippet",
    "Get rid of that code snippet",
    "Remove that piece of code",
    "Clear out that code snippet",
    "Get rid of that code block",
    "Delete that code snippet",
    "Scrap that code segment",
    "Get rid of that code segment",
    "Remove that code fragment",
    "Clear out that code fragment",
    "Trash that code snippet",
    "Get rid of that little bit of code",
    "Take out that chunk of code",
    "Ditch that piece of code",
    "Chuck that code out",
    "Cut that bit of code loose",
    "Toss that piece of code",
    "Trash that bit of code",
    "Get rid of that code snippet",
    "Dispose of that code",
    "Bin that bit of code"
  ]


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
