# Classify a character: Alphabet, Digit, or Special Character.


def classify(ch):
    if ch.isalpha():
        print(f"\n{ch} is Alphabet.")
    elif ch.isdigit():
        print(f"\n{ch} is Digit.")
    else:
        print(f"\n{ch} is Special Character.")


char = input("Enter the character: ")

classify(char)
