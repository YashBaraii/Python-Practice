# Use map() to round off a list of floats.

round_off = lambda n: round(n)

lst_of_floats = [1.1, 1.3, 1.4999, 1.7, 1.9]

print("\nList of floats: ", lst_of_floats)
round_lst_of_floats = list(map(round_off, lst_of_floats))

print("Round off list of floats: ", round_lst_of_floats)
