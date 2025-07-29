# Create a login system: ask for username and password, and check against hardcoded values.

users = [
    {
        "id": 1,
        "username": "Yash",
        "email": "yash@gmail.com",
        "password": "Yash@1234",
    },
    {
        "id": 2,
        "username": "Ram",
        "email": "ram@gmail.com",
        "password": "ram@1234",
    },
]


def authenticate(username, password):
    does_user_exist = False
    is_password_matched = False
    user_id = None

    for user in users:
        if username == user.get("username"):
            does_user_exist = True
            user_id = user.get("id")

    if does_user_exist == False:
        print("\nUser not found !")
        return

    for user in users:
        if user.get("id") == user_id:
            if password == user.get("password"):
                is_password_matched = True

    if is_password_matched == False:
        print("\nIncorrect Password !")
        return
    else:
        print("\nLogin successfull !")


def auth(username, password):
    for user in users:
        if user["username"] == username:
            if user["password"] == password:
                print("\nLogin Successfull !")
                return True
            else:
                print("\nIncorrect Password !")
                return False
    print("\nUser not found !")
    return False


username = input("\nEnter your username: ")
password = input("Enter your password: ")

auth(username, password)
