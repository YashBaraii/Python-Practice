# Count how many times a character appears in a string.


def count_char(st, char):
    st = st.lower()
    char = char.lower()
    count = 0
    for ch in st:
        if ch == char:
            count += 1
    return count


st = "Hey there, myself Yash Barai. I live in Los Angelas"
print("Original String: ", st)

char = input("\nEnter char to check its count (x): ")


print(f"\n'{char}' appears {count_char(st, char)} times in the string.")
