# Function that accepts a string and returns it reversed.


def reverse(st):
    return st[::-1]


st = input("\nEnter something: ")

print(f"Its reversed form is: ", reverse(st))
