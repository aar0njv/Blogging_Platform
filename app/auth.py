#register a user with userid and password.
#passwords are hashed using bcrypt before storing.
#login verifies password using bcrypt's checkpw().


import bcrypt
from app import models
from app.utils import hash_password, check_password

def register_user(username, password):
    """Register a new user if username doesnt exist already."""
    if username in models.users_dict:
        print("Username already taken, try a different one.")
        return False
    hashed_pw = hash_password(password)
    models.users_dict[username] = hashed_pw
    print("User {} registered successfully.".format(username))
    return True


def login_user(username, password):
    if username not in models.users_dict:
        print("User does not exist.")
        return False
    
    stored_hash = models.users_dict[username]

    if (check_password(password, stored_hash)):
        print("Welcome back, {}".format(username))
        return True
    else:
        print("Incorrect password.")
        return False