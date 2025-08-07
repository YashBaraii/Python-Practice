# Recursive function to reverse a string


def reverse(st):
    if len(st) == 0:
        return ""
    return st[-1] + reverse(st[:-1])


st = input("\nEnter something: ")

print(f"Its reversed form is: {reverse(st)}")
