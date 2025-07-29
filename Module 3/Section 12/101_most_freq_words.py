# Write a function that accepts a sentence and returns the most frequent word.

import string


def most_freq_words(st):
    st = st.lower()
    st = "".join([ch for ch in st if ch not in string.punctuation])
    words_count = {}
    for word in st.split():
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return [word for word, count in words_count.items() if count > 1]


sentence = "Hello, man. hello, dude. What is going on. Dude are you okay. Thatswhy dude was so calm. How are you man. What is happening here ?"

print("\nSentence: ", sentence)

freq_words = most_freq_words(sentence)
print("Here are the most frequently occured words: ", *freq_words)
