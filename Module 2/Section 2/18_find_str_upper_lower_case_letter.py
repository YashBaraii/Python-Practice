# Determine if a string has both uppercase and lowercase letters.


def check(st):
    is_upper = False
    is_lower = False
    for ch in st:
        if ch.isupper():
            is_upper = True
        if ch.islower():
            is_lower = True
        if is_lower and is_upper:
            break
    return is_lower and is_upper


def check2(st):
    return any(ch.isupper() for ch in st) and any(ch.islower() for ch in st)


check22 = lambda st: any(ch.islower() for ch in st) and any(ch.isupper() for ch in st)

st = input("Enter the string: ")

if check22(st):
    print("\nYes, It have both uppercase and lowercase letters.")
else:
    print("\nNo, It don't have both uppercase and lowercase letters.")
