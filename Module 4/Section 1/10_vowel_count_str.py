# Function that counts vowels in a string.


def count_vowel(st):
    return sum([1 for ch in st if ch.lower() in "aeiou"])


st = input("\nEnter something: ")
print(f"The total no of vowels in above string is: {count_vowel(st)}")
