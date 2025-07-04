# docs
# is_valid_email(),
# is_valid_egyptian_phone()
# load_users(), 
# save_users(), 
# email_exists()
import json # read json files that store the data
import os # check if file exist
import re # read validation

USERS_FILE = "data/users.json"

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_egyptian_phone(phone):
    return re.match(r"^01[0-2,5]{1}[0-9]{8}$", phone)

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def email_exists(email):
    users = load_users()
    for user in users:
        if user["email"] == email:
            return True
    return False
