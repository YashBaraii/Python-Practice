# Count how many times the word "python" appears in a sentence.

import re


def count_python(st):
    st = st.lower()
    st = re.sub(r"[^\w\s]", "", st)
    words = st.split(" ")
    return sum(1 for word in words if word == "python")


st = "Hello, I like Python so much. And python, is my favourite language"

print(f"\nSentence: \n{st}")
print(f"The word 'python' appears {count_python(st)} times in this sentence. ")
