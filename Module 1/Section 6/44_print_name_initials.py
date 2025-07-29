# Ask for first name, last name and print initials.


def print_initials(fn, ln):
    print("\nThe Initials for your name is: ", fn[0].upper() + ln[0].upper())


first_name = input("\nEnter your first name: ")
last_name = input("Enter your last name: ")

print_initials(first_name, last_name)
