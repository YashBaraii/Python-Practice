# Group words by their lengths using a dictionary.


def group_words(words):
    words = sorted(words, key=len)
    dict = {}
    for word in words:
        length = len(word)
        if length not in dict:
            dict[length] = []
        dict[length].append(word)
    return dict


words = ["Apple", "Banana", "cat", "car", "camera", "bus", "Stand", "stop"]

dict = group_words(words)

print("\nDictionary: ")
for k, v in dict.items():
    print(f"{k} : {v}")
