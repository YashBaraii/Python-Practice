# Build a system that stores movie ratings (title: rating)

import json
from os.path import exists

FILE = "94_movie_data.json"


def load_data():
    if exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(movie_data):
    with open(FILE, "w") as f:
        json.dump(movie_data, f, indent=4)


movie_data = load_data()


def show_data(movie_data):
    print("\n--- Show data: ")

    i = 1
    for key in movie_data.keys():
        print(f"{i}. {key} - Rating ({movie_data[key]})")
        i += 1
    print()


def add_data(movie_data):
    print("\n--- Add data: ")

    movie_name = input("-> Enter movie name: ")
    try:
        movie_rating = float(input(f"-> Enter {movie_name}'s rating out of 10: "))
    except ValueError:
        print("\n--- Err: Please provide valid integer choice!")

    movie_data[movie_name] = movie_rating
    print(f"\nSuccessfully added {movie_name} in the database.")
    save_data(movie_data)


def update_data(movie_data):
    print("\n--- Update data: ")

    movie_name = input("-> Enter movie name: ")
    for key in movie_data.keys():
        if movie_name == key:
            try:
                movie_rating = float(
                    input(f"-> Enter {movie_name}'s updated rating out of 10: ")
                )
            except ValueError:
                print("\n--- Err: Please provide valid integer choice!")

            movie_data[movie_name] = movie_rating
            print(f"\nSuccessfully updated {movie_name}'s rating in database.")
            save_data(movie_data)
            return
    print("\n--- Err: Movie not found!")


def delete_data(movie_data):
    print("\n--- Delete data: ")

    movie_name = input("-> Enter movie name: ")
    for key in movie_data.keys():
        if movie_name == key:

            movie_data.pop(movie_name)
            print(f"\nSuccessfully deleted {movie_name} from database.")
            save_data(movie_data)
            return
    print("\n--- Err: Movie not found!")


try:
    while True:

        print("\n1. Show Data")
        print("2. Add Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. EXIT")

        try:
            choice = int(input("-> Enter your choice: "))
        except ValueError:
            print("\n--- Err: Please provide valid integer choice!")
            continue

        match (choice):
            case 1:
                show_data(movie_data)
            case 2:
                add_data(movie_data)
            case 3:
                update_data(movie_data)
            case 4:
                delete_data(movie_data)
            case 5:
                save_data(movie_data)
                print("\nExiting data !\n")
                break
            case _:
                print("\nErr: Invalid Choice Entered!")

except KeyboardInterrupt:
    print("\n\n🛑 Program interrupted by user! Saving and Exiting the program.")
    save_data(movie_data)
