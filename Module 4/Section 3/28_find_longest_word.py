# Function that returns the longest word in a sentence.
import string


def find_longest_word(st):
    st = "".join([ch for ch in st if ch not in string.punctuation])
    word = max(st.split(), key=len)
    return word, len(word)


st = input("\nEnter something: ")
word, length = find_longest_word(st)
print(f"The Longest word in the above string is: {word} with length: {length}")
