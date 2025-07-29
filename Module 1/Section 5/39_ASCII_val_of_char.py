# Print ASCII value of a character.


def ascii_value(char):
    if len(char) != 1:
        raise ValueError("Input must be a single character")
    return ord(char)


ch = input("\nEnter the character (x): ")
print(f"\nIts ASCII value is: {ascii_value(ch)}")
