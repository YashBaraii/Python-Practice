# Count how many vowels are in a word.


def count(word):
    count = 0
    for l in word.lower():
        if l in {"a", "e", "i", "o", "u"}:
            count += 1

    return count


word = input("\nEnter your word: ")

print(f"The total number of vowels in word {word} is: {count(word)}")
