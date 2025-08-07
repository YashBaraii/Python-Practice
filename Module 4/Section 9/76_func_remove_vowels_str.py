# Function that removes all vowels from a string


def remove_vowels(st):
    return "".join([ch for ch in st if ch not in "aeiouAEIOU"])


st = input("\nEnter something: ")
print(f"\nThe string without vowels: ", remove_vowels(st))
