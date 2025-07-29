# Validate a basic email (contains '@' and '.').


def is_valid(email):
    return "@" in email and "." in email


email = input("\nEnter your email: ")

if is_valid(email):
    print("Yes, your email is valid.")
else:
    print("No, your email is not valid.")
