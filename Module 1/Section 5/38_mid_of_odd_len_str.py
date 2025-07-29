# Extract the middle character from an odd-length string.


def find_mid(st):
    l = len(st)
    if not l & 1:
        raise ValueError("String length is not odd")

    return st[l // 2]


st = input("\nEnter your string: ")
print(f"Its middle character is: {find_mid(st)}")
