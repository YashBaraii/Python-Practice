# Create a set of unique characters from a string.


def unique_chars(st):
    st = st.lower()
    ch_counts = {}
    for ch in st:
        if ch in ch_counts:
            ch_counts[ch] += 1
        else:
            ch_counts[ch] = 1
    return set([key for key, value in ch_counts.items() if value == 1])


st = input("\nEnter the string: ")
set = unique_chars(st)
print("This is a set of unique characters in string: ", set)
