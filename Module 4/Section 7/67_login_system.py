# Function to simulate a login system (username/password check)

users = {"user": "user1234", "user2": "user21234"}

is_authenticated = False


def login(username, password):

    global is_authenticated

    if username not in users:
        print("\nUser not found!")
        return

    if users[username] == password:
        print("\nLogin credentials matched!")
        is_authenticated = True
        return
    else:
        print("\nIncorrect Password!")


while True:
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    login(username, password)

    if is_authenticated:
        break
