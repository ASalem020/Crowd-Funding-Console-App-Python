# docs
# register():           # Validates input, checks email/phone, saves new user
# login():              # Authenticates email + password

from utils import load_users, save_users, is_valid_email, is_valid_egyptian_phone, email_exists
from getpass import getpass



def register():
    print("\n--- Register ---")

    # First Name
    for _ in range(3):
        first_name = input("First Name: ")
        if first_name:
            break
        print("❌ First name cannot be empty.")
    else:
        print("⚠️ Too many failed attempts. Returning to main menu.")
        return

    # Last Name
    for _ in range(3):
        last_name = input("Last Name: ")
        if last_name:
            break
        print("❌ Last name cannot be empty.")
    else:
        print("⚠️ Too many failed attempts. Returning to main menu.")
        return

    # Email
    for _ in range(3):
        email = input("Email: ")
        if not is_valid_email(email):
            print("❌ Invalid email format.")
            continue
        if email_exists(email):
            print("❌ Email already registered.")
            continue
        break
    else:
        print("⚠️ Too many failed attempts. Returning to main menu.")
        return

    # Password + Confirm
    for _ in range(3):
        password = getpass("Password: ")
        confirm_password = getpass("Confirm Password: ")
        if password == confirm_password and password:
            break
        print("❌ Passwords do not match or empty.")
    else:
        print("⚠️ Too many failed attempts. Returning to main menu.")
        return

    # Egyptian Phone
    for _ in range(3):
        phone = input("Mobile (Egyptian format): ")
        if is_valid_egyptian_phone(phone):
            break
        print("❌ Invalid Egyptian phone number.")
    else:
        print("⚠️ Too many failed attempts. Returning to main menu.")
        return

    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone
    }

    users = load_users()
    users.append(user_data)
    save_users(users)

    print("✅ Registration successful! You can now log in.")


def login():
    print("\n--- Login ---")
    
    for _ in range(3):
        email = input("Email: ")
        password = getpass("Password: ")

        if not is_valid_email(email):
            print("❌ Invalid email format.")
            continue

        users = load_users()
        for user in users:
            if user["email"] == email and user["password"] == password:
                print(f"✅ Welcome, {user['first_name']}!")
                return user

        print("❌ Incorrect email or password.")
    else:
        print("⚠️ Too many failed attempts. Returning to main menu.")
        return None



