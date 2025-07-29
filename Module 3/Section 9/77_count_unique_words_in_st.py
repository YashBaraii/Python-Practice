# Count the number of unique words in a sentence.

import string


def count_unique(st):
    st = st.lower()
    st = "".join([ch for ch in st if ch not in string.punctuation])
    counts = {}
    for word in st.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return sum([1 for key, value in counts.items() if value == 1])


st = input("\nEnter something: ")
print(f"In this sentence the no. of unique words is: {count_unique(st)}.")
