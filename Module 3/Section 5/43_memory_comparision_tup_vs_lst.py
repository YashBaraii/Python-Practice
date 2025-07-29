# Compare memory usage between a list and a tuple.

from sys import getsizeof

tup = (1, 2, 3)
lst = [1, 2, 3]

print(f"List: {lst} and Tuple: {tup}")

print(f"\nThe Memory occupied by the tuple is: {getsizeof(tup)} bytes.")
print(f"The Memory occupied by the list is: {getsizeof(lst)} bytes.")
