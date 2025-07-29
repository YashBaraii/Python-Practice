# Count uppercase vs lowercase characters.


def count_uppercase_lowercase(st):
    upp_count = low_count = 0
    for ch in st:
        if ch.isupper():
            upp_count += 1
        elif ch.islower():
            low_count += 1
    return upp_count, low_count


st = input("\nEnter something: ")
uppercase_count, lowercase_count = count_uppercase_lowercase(st)
print(
    f"Total uppercase and lowercase characters in this string are: {uppercase_count} and {lowercase_count} respectively."
)
