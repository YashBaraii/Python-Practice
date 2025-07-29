# Create a contact book using a dictionary (name: phone number).

import json
from os.path import exists

FILE = "91_contacts.json"


def load_data():
    if exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(contact_book):
    with open(FILE, "w") as f:
        json.dump(contact_book, f, indent=4)


contact_book = load_data()


def show_contacts(contact_book):
    print("\n--- All contacts:\n")
    i = 1
    for name, contact in contact_book.items():
        print(f"{i}. {name} - {contact}")
        i += 1
    print()


def get_contact(contact_book):
    print("\n--- Get contact by name:\n")
    try:
        name = input("Enter the name of contact: ")
    except ValueError:
        print("--- Err: Input must be string and valid")

    i = 1
    retrived_count = 0
    print()
    for key in contact_book.keys():
        if name.lower() in key.lower() or name.lower() == key.lower():
            print(f"{i}. {key} - {contact_book[key]}")
            retrived_count += 1

        i += 1
    if retrived_count == 0:
        print("\nErr: Contact not found!")


def add_contact(contact_book):
    print("\n--- Manage Contact > Add Contact:\n")

    try:
        name = input("Enter the name of contact: ")
    except ValueError:
        print("--- Err: Input must be string and valid")

    try:
        contact = int(input("Enter the contact number: "))
    except ValueError:
        print("--- Err: Input must be valid phone number!")

    try:
        contact_book[name.title()] = contact
        print(f"\nSuccessfully added {name.title()}'s contact in book\n")
        save_data(contact_book)
    except Exception as e:
        print("--- Err: Unexpected error occured !")
        print(e)


def update_contact(contact_book):
    print("\n--- Manage Contact > Update Contact:\n")

    try:
        name = input("Enter the name of contact: ")
    except ValueError:
        print("--- Err: Input must be string and valid")
        return

    i = 1
    retrieved_count = 0
    print(f"\n--- All contact with name {name.title()}:\n")
    for key in contact_book.keys():
        if name.title() in key or name.title() == key:
            print(f"{i}. {key} - {contact_book[key]}")
            retrieved_count += 1
        i += 1

    if retrieved_count == 0:
        print("\nErr: Contact not found!")
    elif retrieved_count == 1:
        correct_full_name = [key for key in contact_book.keys() if name.title() in key][
            0
        ]
    elif retrieved_count > 1:
        try:
            full_name = input("\nEnter full name to clear the confusion: ")
        except ValueError:
            print("--- Err: Input must be string and valid")

        i = 1
        print(f"\n--- All contact with name {full_name}:\n")
        for key in contact_book.keys():
            if full_name.title() in key or full_name.title() == key:
                print(f"{i}. {full_name} - {contact_book[key]}")
                correct_full_name = key
            i += 1
    try:
        contact = int(input("Enter the contact number: "))
    except ValueError:
        print("--- Err: Input must be valid phone number!")

    try:
        contact_book[correct_full_name] = contact
        print(f"\nSuccessfully updated {correct_full_name.title()}'s contact in book\n")
        save_data(contact_book)
    except Exception as e:
        print("--- Err: Unexpected error occured !")
        print(e)


def delete_contact(contact_book):
    print("\n--- Manage Contact > Delete Contact:\n")

    try:
        name = input("Enter the name of contact: ")
    except ValueError:
        print("--- Err: Input must be string and valid")
        return

    i = 1
    retrieved_count = 0
    print(f"\n--- All contact with name {name.title()}:\n")
    for key in contact_book.keys():
        if name.title() in key or name.title() == key:
            print(f"{i}. {key} - {contact_book[key]}")
            retrieved_count += 1
        i += 1

    if retrieved_count == 0:
        print("\nErr: Contact not found!")
    elif retrieved_count == 1:
        correct_full_name = [key for key in contact_book.keys() if name.title() in key][
            0
        ]
    elif retrieved_count > 1:
        try:
            full_name = input("\nEnter full name to clear the confusion: ")
        except ValueError:
            print("--- Err: Input must be string and valid")

        i = 1
        print(f"\n--- All contact with name {full_name}:\n")
        for key in contact_book.keys():
            if full_name.title() in key or full_name.title() == key:
                print(f"{i}. {full_name} - {contact_book[key]}")
                correct_full_name = key
            i += 1

    try:
        contact_book.pop(correct_full_name)
        print(f"\nSuccessfully deleted {correct_full_name.title()}'s contact in book\n")
        save_data(contact_book)
    except Exception as e:
        print("--- Err: Unexpected error occured !")
        print(e)


def manage_contact(contact_book):
    print("\n--- Manage Contact:\n")

    while True:
        print("\n1. Add contact")
        print("2. Update contact")
        print("3. Delete contact")
        print("4. Go to HOME")

        try:
            choice = int(input("--> Enter your choice: "))
        except ValueError:
            print("\nErr: Input must be an integer!")

        match (choice):
            case 1:
                add_contact(contact_book)

            case 2:
                update_contact(contact_book)

            case 3:
                delete_contact(contact_book)

            case 4:
                break


print("\n---- CONTACT BOOK ----\n")

while True:
    print("\n1. Show all contact")
    print("2. Get contact by name")
    print("3. Manage Contact")
    print("4. EXIT ")

    try:
        choice = int(input("-> Enter your choice: "))
    except ValueError:
        print("\nErr: Input must be an integer!")

    match (choice):
        case 1:
            show_contacts(contact_book)

        case 2:
            get_contact(contact_book)

        case 3:
            manage_contact(contact_book)

        case 4:
            print("\nExiting the script!\n\n")
            save_data(contact_book)
            break
