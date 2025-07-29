# Demonstrate the immutability of tuples.

tup = (1, 2, 3, 4, 5)
lst = [1, 2, 3, 4, 5]

print(f"\nTuple: {tup} and List: {lst}")

lst[0] = 0
print("\nList after changing first element: ", lst)

print("Tuple after changing first elment:")
tup[0] = 0
