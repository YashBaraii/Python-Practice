# Function that counts occurrences of each character in a string.


def count_ch(st):
    st = st.lower()
    ch_counts = {}
    for ch in st:
        if ch in ch_counts:
            ch_counts[ch] += 1
        else:
            ch_counts[ch] = 1
    return ch_counts


st = input("\nEnter something: ")
counts = count_ch(st)

print()
for k, v in counts.items():
    print(f"{k} occurs {v} times in the string")
