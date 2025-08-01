# Use reduce() to find the maximum element.

from functools import reduce

lst = [1, 2, 335, 4, 5]

print(f"\nList: {lst}")

print(
    f"The maximum of all the elements in the above list is: {reduce(lambda a, b: max(a, b), lst)}"
)
