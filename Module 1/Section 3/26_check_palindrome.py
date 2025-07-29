# Check if a string is a palindrome (e.g., "madam").

original_st = input("Enter your string: ")
st = original_st.lower()

filterd = "".join(char for char in st if char.isalnum())

if not filterd:
    print("String is empty !")
else:
    reverse = filterd[::-1]
    if filterd == reverse:
        print(f"\n{original_st} is a palindrome.")
    else:
        print(f"\n{original_st} is not a palindrome.")
