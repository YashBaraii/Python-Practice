# Create a greeting program that takes the user's name and age


def greet():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print("\nHello ", name)
    if age > 18:
        print("\nYou are eligible to drive.")
    else:
        print("\nYou aren't eligible to drive.")


greet()
