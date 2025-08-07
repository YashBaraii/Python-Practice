# Function that capitalizes each word in a sentence.


def capitalize_words(st):
    return " ".join([word.capitalize() for word in st.split()])


sentence = "hello world! welcome to python."
print(f"\nOriginal sentence: \n", sentence)
print(f"\nSentence after caplitalizing each word: \n{capitalize_words(sentence)}")
