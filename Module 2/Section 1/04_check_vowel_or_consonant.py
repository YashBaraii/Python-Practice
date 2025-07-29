# Check if a character is a vowel or consonant.


def is_vowel(ch):
    ch = ch.lower()
    if ch in ["a", "e", "i", "o", "u"]:
        return True
    return False


is_vowel2 = lambda ch: True if ch.lower() in ["a", "e", "i", "o", "u"] else False

char = input("Enter the character: ")

if is_vowel2(char):
    print(f"{char} is the vowel.")
else:
    print(f"{char} is the consonant.")
