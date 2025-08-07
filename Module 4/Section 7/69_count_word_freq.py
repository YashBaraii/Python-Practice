# Function to count frequency of words in a string.

import string


def count_word(st, w):
    w = w.lower()
    st = st.lower()
    st = "".join([ch for ch in st if ch not in string.punctuation])
    count = 0

    for word in st.split():
        if w == word:
            count += 1
    return count


st = "The quick brown fox jumps over the lazy dog. Then the dog, the lazy dog, chases the fox again. The quick brown fox, now tired, rests near the dog, the same d_og it had previously played with. This cycle of the quick, the lazy, and the quick, often repeats itself. "


print("\nString: \n", st)

word = input("\nEnter the word to find its frequency in this string: ")

print(f"The word {word} appears {count_word(st, word)} times in the string.")
