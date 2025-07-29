# Count frequency of characters in a string.


def count_freq(st):
    st = st.lower()
    counts = {}
    for ch in st:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts


st = input("\nEnter something: ")

count_freqencies = count_freq(st)
print("The frequency count of each char in string: \n")

for key, value in count_freqencies.items():
    print(f"{key}: {value}", end=". ")
