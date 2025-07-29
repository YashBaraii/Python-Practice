# ATM Simulator: Enter PIN → Show Menu (Withdraw, Balance, Exit).

import json
from os.path import exists

FILE = "96_ATM_users.json"


def load_users():
    if exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=2)


users = load_users()

is_card_inserted = False
MAX_PIN_TRIES = 3
pin_tries_count = 0
is_user_authorized = False
user_id = -1


def get_username(user_id):
    for user in users:
        if user["id"] == user_id:
            return user["username"]
    return "xyz"


def is_pin_valid(pin):
    global pin_tries_count, user_id
    pin_tries_count += 1

    if len(str(pin)) != 4 or not str(pin).isdigit():
        print("\n--- Err: Pin must be exactly 4 digits.")
        return False

    for user in users:
        if user["pin"] == pin:
            user_id = user["id"]
            return True

    return False


def get_balance(user_id):
    for user in users:
        if user["id"] == user_id:
            return user["balance"]


def deduct_balance(user_id, amount):
    for user in users:
        if user["id"] == user_id:
            if user["balance"] < amount:
                return False
            user["balance"] -= amount
            return True
    return False


def authorize_user():
    global pin_tries_count, is_user_authorized, user_id
    while True:
        if pin_tries_count >= MAX_PIN_TRIES:
            print("\n--- Pin trying limit reached. Please try again later.")
            break

        try:
            pin = int(input("\nEnter your 4-digit pin (0000): "))
        except ValueError:
            print("\n--- Invalid input. Please enter digits only.")
            continue

        if is_pin_valid(pin):
            is_user_authorized = True
            print(f"\n--- Welcome back {get_username(user_id)}")
            print("\n-- Pin authorized successfully!")
            break
        else:
            print(
                f"\n--- Err: Unauthorized access | Please enter the correct pin\n-- You have only {MAX_PIN_TRIES - pin_tries_count} attempts left."
            )


def check_balance(user_id):
    balance = get_balance(user_id)
    print(f"\nDear {get_username(user_id)}, your current account balance: ₹ {balance}")


def withdraw(user_id):
    try:
        amount = int(input("\nEnter amount to withdraw: "))
    except ValueError:
        print("\n--- Please enter a valid numeric amount!")
        return

    if amount <= 0:
        print("\n--- Withdrawal amount must be greater than 0.")
        return

    if deduct_balance(user_id, amount):
        save_users(users)
        print(f"\n₹{amount} have been successfully withdrawn.")
    else:
        print(f"\n--- Err: Insufficient balance, can't withdraw money.")


def main():
    global is_card_inserted
    print(
        "\n------------\nWelcome to APNA ATM | We provide reliable ATM services\n------------\n"
    )
    while True:
        if not is_card_inserted:
            card = input("\nHave you inserted your respective card (Y/N): ")
            if card.lower() != "y":
                print("Please insert your ATM CARD!")
                continue
            is_card_inserted = True

        if pin_tries_count >= MAX_PIN_TRIES:
            break

        if not is_user_authorized:
            authorize_user()
            if not is_user_authorized:
                break

        print("\n----- Available Services -----\n")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Exit")

        try:
            choice = int(input("-> What service would you like to use? e.g. (1): "))
        except ValueError:
            print("\n--- Please enter the number before the service option.")
            continue

        match choice:
            case 1:
                check_balance(user_id)
            case 2:
                withdraw(user_id)
            case 3:
                print("\n\n--- Thanks for choosing us! ")
                break
            case _:
                print("\n--- Invalid choice. Please select a valid option.")


main()
