# Find the index of an element in a tuple.

find_index = lambda tup, e: list(tup).index(e)

tup = (1, 3, 2, 2, 1, 4, 1, 5)
print(f"Tuple: {tup}")

num = int(input("\nEnter the element to find its index: "))
print(f"'{num}' appears at the index {find_index(tup, num)} in the tuple.")
