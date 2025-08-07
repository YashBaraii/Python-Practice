# Function that unpacks a list of tuples and returns two separate lists.

unpack_tuples = lambda pairs: zip(*pairs)


pairs = [(1, "a"), (2, "b"), (3, "c")]

nums, letters = unpack_tuples(pairs)

print(f"\nThe pairs: ", *pairs)

print("Numbers:", nums)
print("Letters:", letters)
