# Create an inventory system using a dictionary

import json
from os.path import exists

FILE = "90_inventory_data.json"


def load_data():
    if exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(inventory):
    with open(FILE, "w") as f:
        json.dump(inventory, f)


inventory = load_data()


def show_inventory(inventory):
    print("\n--- Inventory: ")
    i = 1
    for item, quantity in inventory.items():
        print(f"    {i}. {item} x {quantity}")
        i += 1
    print()


def add_item(inventory):

    print("\n----- Manage Inventory > Add Item: ")

    try:
        item = input("\nEnter the name of item: ")
        quantity = int(input(f"Enter {item}'s quantity: "))
    except ValueError:
        print("\nErr: Please enter valid data !")
    except Exception as e:
        print("\nErr: ", e)

    try:
        inventory[item.lower()] = quantity
        print(f"\n---{item} successfully added into inventory\n")
        save_data(inventory)
    except Exception as e:
        print("\nErr: Unexpected error occured !")
        print(e)


def update_item(inventory):
    print("\n----- Manage Inventory > Update Item Quantity: ")

    try:
        item = input("\nEnter the name of item: ")
        if item.lower() in inventory:
            quantity = int(input("\nEnter the new quantity: "))
            inventory[item.lower()] = quantity
            print(f"\n--- Successfully updated {item}'s quantity !\n")
            save_data(inventory)
        else:
            print("\nErr: Item not found !")
    except ValueError:
        print("\nErr: Please enter valid data !")
    except Exception as e:
        print("\nErr: ", e)


def delete_item(inventory):
    print("\n----- Manage Inventory > Delete Item: ")

    try:
        item = input("\nEnter the name of item: ")
        if item.lower() in inventory:
            inventory.pop(item.lower())
            print(f"\n--- Successfully deleted {item} !\n")
            save_data(inventory)
        else:
            print("\nErr: Item not found !")
    except ValueError:
        print("\nErr: Please enter valid data !")
    except Exception as e:
        print("\nErr: ", e)


def manage_inventory(inventory):
    print("\n--- Manage Inventory: \n")
    while True:
        print("1. Add Item")
        print("2. Update Item Quantity")
        print("3. Delete Item")
        print("4. Go to HOME (stop managing)")

        try:
            choice = int(input("--> Enter your choice (x): "))
        except ValueError:
            print("\nErr: Choice must a number show beside options !\n")

        match (choice):
            case 1:
                add_item(inventory)
            case 2:
                update_item(inventory)
            case 3:
                delete_item(inventory)
            case 4:
                break


print("\n---- INVENTORY SYSTEM ----\n")
try:
    while True:
        print("\n1. Show Inventory")
        print("2. Manage Inventory")
        print("3. EXIT")
        try:
            choice = int(input("-> Enter your choice (x): "))
        except ValueError:
            print("\nErr: Choice must a number show beside options !")

        match (choice):
            case 1:
                show_inventory(inventory)
            case 2:
                manage_inventory(inventory)
            case 3:
                print("\n--- Saving data and exiting the script !\n")
                save_data(inventory)
                break

            case _:
                print("\nErr: Invalid choice. Please select a valid option.")

except KeyboardInterrupt:
    print("\n\n⚠️  Script interrupted by user. Saving data and exiting...")
    save_data(inventory)
