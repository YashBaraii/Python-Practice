# Use reduce() to find the product of a list.

from functools import reduce

lst = [1, 2, 3, 4, 5]

print(f"\nList: {lst}")

print(
    f"The product of all the elements in the above list is: {reduce(lambda a, b: a *b, lst)}"
)
