# Ask the user to enter a sentence and print each word on a new line.


def print_words(st):
    lst = st.split(" ")
    for i in lst:
        print(i)


sentence = input("\nEnter the sentence: \n")
print_words(sentence)
print()
