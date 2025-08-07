#   Function that replaces spaces with hyphens.


def replace_spaces(st):
    words = st.split()
    return "_".join([word for word in words])


st = input("\nEnter something: ")
print("\nString without spaces, instead with hyphen: \n", replace_spaces(st))
