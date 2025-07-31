# Create a function to check if a string is a palindrome.
import string


def is_palindrome(st):
    st = st.lower()
    st = "".join([ch for ch in st if ch not in string.punctuation])
    return st == st[::-1]


st = input("\nEnter something: ")
if is_palindrome(st):
    print(f"{st} is a palindrome")
else:
    print(f"{st} is not a palindrome")
