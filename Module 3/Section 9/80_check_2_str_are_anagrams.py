# Check if two strings are anagrams using sets.


def are_anagrams(st1, st2):
    st1 = st1.replace(" ", "").lower()
    st2 = st2.replace(" ", "").lower()

    if set(st1) != set(st2):
        return False

    for ch in set(st1):
        if st1.count(ch) != st2.count(ch):
            return False

    return True


st1, st2 = map(str, input("\nEnter 2 strings separated by comma: ").split(","))

if are_anagrams(st1, st2):
    print("Yes, these two strings are anagrams.")
else:
    print("No, these two strings aren't anagrams.")
