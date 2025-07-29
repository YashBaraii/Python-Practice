# Create a simple login system with 3 tries.

import json
from os.path import exists

FILE = "66_users.json"


def load_users():
    if exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=2)


users = load_users()

masked_pass = lambda pw: ("*" * (len(pw) - 2)) + pw[-2:]


def is_authenticated(username, password):
    for user in users:
        if user["username"] == username:
            return user["password"] == password
    return -1


def register():
    print("\nRegistering User:\n")
    username = input("Enter your username: ")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    if any(user["username"] == username or user["email"] == email for user in users):
        print("Username or email already exists.")
        return

    new_user = {
        "id": len(users) + 1,
        "username": username,
        "email": email,
        "password": password,
    }

    users.append(new_user)

    save_users(users)

    print("\n--- User is successfully registered!")

    print(f"\nYour credentials :")
    print(f"-> Username: {username}")
    print(f"-> Email: {email}")
    print(f"-> Password: {masked_pass(password)}\n")


def login():
    max_tries = 3
    count = 1

    print("\n--- User Login: ---\n")

    while True:
        if count > max_tries:
            print("\n --- Login limit reached | Please try again later !")
            break

        username = input("\nEnter your username: ")
        password = input("Enter your password: ")

        auth_result = is_authenticated(username, password)

        if auth_result is True:
            print("\nWelcome back user !\n")
            dashboard()
            break

        elif auth_result == -1:
            print("\nUser not found !\n")

        else:
            print("\nIncorrect credentials !")
            print(f"--- You have only {max_tries - count} attempts left !")

        count += 1


def dashboard():
    print("\n--- Hello User, welcome to the dashboard ! ---")


while True:

    print("\nLogin System: \n")
    print("1. Register")
    print("2. Login")
    print("3. EXIT !")

    choice = int(input("Enter your choice (x): "))

    match (choice):
        case 1:
            register()
        case 2:
            login()
        case 3:
            break
        case _:
            print("Invalid choice selected !")
