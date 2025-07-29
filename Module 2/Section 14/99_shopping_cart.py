# Shopping Cart: Loop to input items → total → checkout.

items = [
    {"id": 1, "name": "Smartphone", "price": 20000},
    {"id": 2, "name": "Shirt", "price": 599},
    {"id": 3, "name": "Book", "price": 100},
    {"id": 4, "name": "Bread", "price": 50},
    {"id": 5, "name": "Pen", "price": 20},
]

selected_items = []


def browse_product():
    print("\n-- Browsing products: \n")
    for item in items:
        print(f"{item["id"]}. {item["name"]} for ₹ {item["price"]}.")

    item_selection = int(
        input("\n-> Which item do you want to add in your cart? (x): ")
    )

    for item in items:
        if item["id"] == item_selection:
            selected_items.append(item)

    browse_prod_again = input("\nWant to browse products again ? (Y/N): ")

    if browse_prod_again.lower() == "y":
        browse_product()
    else:
        return


def total_selected_items():
    total = sum(item["price"] for item in selected_items)
    print(f"\nThe Total of all selected items is: {total}")


def checkout():
    print(f"\nYour purchased items: ")
    for item in selected_items:
        print(f"{item["id"]}. {item["name"]} for ₹ {item["price"]}.")


print("\n----- Shopping Cart System -----\n")
while True:
    print("\n1. Browse Products")
    print("2. Total")
    print("3. Checkout")
    print("4. EXIT")
    choice = int(input("-> Enter your choice (x): "))

    match (choice):
        case 1:
            browse_product()
        case 2:
            total_selected_items()
        case 3:
            checkout()
        case 4:
            print("\nThank you for shopping with us !")
            break
