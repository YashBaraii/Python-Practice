#  Use reduce() to concatenate strings in a list.

from functools import reduce

lst_of_strs = ["Hi,", "How", "are", "you", "?"]

print(f"\nList: ", lst_of_strs)

concatenated = reduce(lambda x, y: x + " " + y, lst_of_strs)

print("Its concatenated version is: ", concatenated)
