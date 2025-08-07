#  Function to generate a password from name and DOB

import random


def generate_password(info):
    chars = ["@", "#", "*", "$", "₹", "&", "%", "^"]
    password = info["name"].title() + random.choice(chars) + info["dob"][-4:]
    return password


name = input("\nEnter your name: ")
while True:
    dob = input("Enter your Date of birth (DD/MM/YYYY): ")

    if len(dob) == 10 and dob.count("/") == 2:
        break

info = {"name": name, "dob": dob}

generated_password = generate_password(info)

print("\nYour generated password is: ", generated_password)
