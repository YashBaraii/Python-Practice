# Make a language dictionary (EN → FR) with 5 words.


import json
from os.path import exists

FILE = "95_lang_dict.json"


def load_data():
    if exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(lang_dict):
    with open(FILE, "w") as f:
        json.dump(lang_dict, f, indent=4)


lang_dict = load_data()


def show_dict(lang_dict):
    print("\n--- Show Dictionary: ")

    i = 1
    print(" English  ->  French")
    for key in lang_dict.keys():
        print(f"{i}. {key} -> {lang_dict[key]}")
        i += 1
    print()


def translate(lang_dict):
    print("\n--- Translate (en - fr):\n")

    en_word = input("-> Enter English word to translate: ")

    if en_word in lang_dict:
        print(f"\nThe word {en_word} is '{lang_dict[en_word]}' in french.")
    else:
        print(f"\n--- Err: {en_word} not found!")


def add_word(lang_dict):
    print("\n--- Add word: ")

    en_word = input("\nEnter English word: ")
    fr_word = input("Enter its French word: ")

    lang_dict[en_word] = fr_word
    print(f"\nSuccessfully added {en_word} in the database.")
    save_data(lang_dict)


def delete_word(lang_dict):
    print("\n--- Delete word: ")

    en_word = input("-> Enter english word: ")
    if en_word in lang_dict:
        lang_dict.pop(en_word)
        print(f"\nSuccessfully deleted {en_word} from database.")
        save_data(lang_dict)
    else:
        print(f"\n--- Err: {en_word} not found!")


def update_word(lang_dict):
    print("\n--- Update word: ")

    en_word = input("-> Enter English word: ")

    if en_word in lang_dict:
        fr_word = input("Enter its updated French word: ")

        lang_dict[en_word] = fr_word
        print(f"\nSuccessfully updated {en_word}'s rating in database.")
        save_data(lang_dict)

    else:
        print(f"\n--- Err: {en_word} not found!")


print("\n----- LANGUAGE DICT (EN - FR) -----\n")

try:
    while True:

        print("\n1. Show Dictionary")
        print("2. Translate")
        print("3. Add Word")
        print("4. Remove Word")
        print("5. Update Word")
        print("6. EXIT")

        try:
            choice = int(input("-> Enter your choice: "))
        except ValueError:
            print("\n--- Err: Please provide valid integer choice!")
            continue

        match (choice):
            case 1:
                show_dict(lang_dict)
            case 2:
                translate(lang_dict)
            case 3:
                add_word(lang_dict)
            case 4:
                delete_word(lang_dict)
            case 5:
                update_word(lang_dict)
            case 6:
                save_data(lang_dict)
                print("\nExiting data !\n")
                break
            case _:
                print("\nErr: Invalid Choice Entered!")

except KeyboardInterrupt:
    print("\n\n🛑 Program interrupted by user! Saving and Exiting the program.")
    save_data(lang_dict)
