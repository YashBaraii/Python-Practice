# Check if a string has more vowels than consonants.


def is_more_vowels(st):
    vowels_count = 0
    consonants_count = 0

    for ch in st:
        if ch.lower() in {"a", "e", "i", "o", "u"}:
            vowels_count += 1
        else:
            consonants_count += 1
    return vowels_count > consonants_count


st = input("Enter the string: ")

if is_more_vowels(st):
    print("\nString have more vowels than consonants.")
else:
    print("\nString have more consonants than vowels.")
