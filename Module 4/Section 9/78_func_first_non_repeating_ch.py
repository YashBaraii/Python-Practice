#  Function that finds the first non-repeating character.

import string


def find_char(st):
    st = st.lower()
    st = "".join([ch for ch in st if ch not in string.punctuation])
    char_counts = {}

    for ch in st:
        char_counts[ch] = char_counts.get(ch, 0) + 1

    for ch in st:
        if char_counts[ch] == 1:
            return ch

    return None


print(find_char("Swiss"))
print(find_char("repeater"))
print(find_char("aabbcc"))
