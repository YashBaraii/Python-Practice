# Count word frequency in a sentence.

import re
import string


def count_word(st, w):
    st = st.lower()
    st_lst = "".join([ch for ch in st if ch not in string.punctuation]).split()
    return sum([1 for ch in st_lst if ch == w])


def count_word2(st, w):
    st = st.lower()
    st = re.sub(r"[^\w\s]", "", st)
    return sum([1 for ch in st.split() if ch == w])


st = "Hello, dude, Dude how you doing? Are you okay, dude ?"
print(f"\nSentence: {st}")

key = input("\nWhich word's count you want to know? ")

print(f"-> The word {key} appears {count_word2(st, key)} times in this sentence.")
