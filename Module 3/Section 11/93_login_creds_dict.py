# Create a dictionary to store login credentials.

import json
from os.path import exists
import hashlib
import getpass

FILE = "93_login_data.json"


def load_data():
    if exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(login_data):
    with open(FILE, "w") as f:
        json.dump(login_data, f, indent=4)


login_data = load_data()


def show_data(login_data):
    print("\n--- All Login Data: \n")

    i = 1
    for key, value in login_data.items():
        print(f"{i}. {key} - {value}")
        i += 1
    print()


def add_data(login_data):
    print("\n--- Add data --- \n")

    try:
        username = input("\nEnter your username: ")
    except ValueError:
        print("\nErr: Please provide appropriate and valid data !")

    try:
        password = getpass.getpass("\nEnter your password: ")
    except ValueError:
        print("\nErr: Please provide appropriate and valid data !")

    hased_pw = hashlib.sha256(password.encode()).hexdigest()
    login_data[username] = password
    print(f"\nSuccesfully added {username} into login data.")
    save_data(login_data)


def delete_data(login_data):
    print("\n--- Delete data --- \n")

    try:
        username = input("\nEnter your username: ")
    except ValueError:
        print("\nErr: Please provide appropriate and valid data !")

    is_user_found = False

    for key in login_data.keys():
        if username == key:
            is_user_found = True
            break

    if is_user_found:
        try:
            password = input("\nEnter your password to confirm delete: ")
        except ValueError:
            print("\nErr: Please provide appropriate and valid data !")

        login_data.pop(username)
        print(f"\nSuccesfully deleted {username} frmo login data.")
        save_data(login_data)

    else:
        print("\n--- Err: User not found!")


print("\n----- LOGIN CREDS STORAGE -----\n")
try:
    while True:
        print("\n1. Show data")
        print("2. Add data")
        print("3. Delete data")
        print("4. EXIT !")

        try:
            choice = int(input("-> Enter your choice: "))
        except ValueError:
            print("\nErr: Input must be an integer!")

        match (choice):
            case 1:
                show_data(login_data)

            case 2:
                add_data(login_data)

            case 3:
                delete_data(login_data)

            case 4:
                print("\nExiting the script!\n\n")
                save_data(login_data)
                break


except KeyboardInterrupt:
    print("\n\n⚠️  Script interrupted by user. Saving data and exiting...")
    save_data(login_data)
