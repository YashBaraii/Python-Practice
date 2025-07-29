# Count how many words are in a sentence.

count_words = lambda st: len(st.split())

st = input("\nEnter something: ")
print(f"There are total {count_words(st)} words in this string.")
