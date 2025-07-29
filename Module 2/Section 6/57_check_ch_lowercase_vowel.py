# Check if a character is a lowercase vowel.

is_lowercase_vowel = lambda ch: ch in {"a", "e", "i", "o", "u"}

char = input("Enter your character: ")

if is_lowercase_vowel(char):
    print("Yes, it is lowercase vowel.")
else:
    print("No, it is not lowercase vowel.")
