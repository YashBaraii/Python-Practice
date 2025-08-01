#   Use map() to convert a list of strings to uppercase

convert = lambda st: st.upper()

lst_of_strs = ["hi,", "How", "arE", "you", "?"]
print("\nList of strings: ", lst_of_strs)

uppercase_lst_of_strs = list(map(convert, lst_of_strs))
print("\nUppercase List of strings: ", uppercase_lst_of_strs)
