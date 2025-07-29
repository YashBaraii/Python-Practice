# Replace all vowels in a string with '*'.


def replace_vowel(st):
    for ch in st:
        if ch.lower() in {"a", "e", "i", "o", "u"}:
            st = st.replace(ch, "*")
    return st


replace_vowel2 = lambda st: "".join("*" if ch.lower() in "aeiou" else ch for ch in st)

st = input("\nEnter something: ")

print(
    f"After replacing vowels to '*', the string looks like this: {replace_vowel2(st)}"
)
