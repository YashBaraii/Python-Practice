# From a list of words, find those with unique letters.

is_unique = lambda w: sum([1 for ch in w.lower() if w.lower().count(ch) == 1]) == len(w)


def find_words(words):
    return [word for word in words if is_unique(word)]


words = ["ApPle", "Banana", "cat", "car", "camera", "bus", "Stand", "stop"]

print("\nWords: ", *words)

unique_letters_words = find_words(words)
print("The words whose letters are unique: ", *unique_letters_words)
