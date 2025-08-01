# Use filter() to extract palindromes from a list

import string


def is_palindrome(ele):
    st_ele = str(ele).lower()
    st_ele = (
        "".join([ch for ch in st_ele if ch not in string.punctuation])
        .strip()
        .replace(" ", "")
    )
    return st_ele[::-1] == st_ele


lst = ["level", "race car, -", 12321, "race ,", "dog"]

print(f"\nList containing palindromes: {lst}")

palindromes = list(filter(is_palindrome, lst))
print("Here is the list of palindromes: ", palindromes)
