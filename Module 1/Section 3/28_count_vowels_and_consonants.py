# Take user input and count vowels and consonants.


def count_vowels_and_consonants(st):
    st = st.lower()
    vowels = {"a", "e", "i", "o", "u"}
    vowels_count = 0
    consonants_count = 0

    for ch in st:
        if ch.isalpha():
            if ch in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    return vowels_count, consonants_count


st = "Hey there, myself Yash Barai. I live in Los Angelas"
print("Original String: ", st)

vowels_count, consonants_count = count_vowels_and_consonants(st)
print(f"\nVowels count in string: {vowels_count}")
print(f"\nConsonants count in string: {consonants_count}")
