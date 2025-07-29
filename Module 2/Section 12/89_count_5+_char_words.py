# Input a sentence and count how many words are longer than 5 characters.


def count_words(st):
    count = 0
    words = st.split()
    for word in words:
        if len(word) > 5:
            count += 1
    return count


count_words2 = lambda st: sum(1 for word in st.split() if len(word) > 5)


st = input("\nEnter something: ")
print(f"The total no of words that are more than 5 chars are: {count_words2(st)}")
