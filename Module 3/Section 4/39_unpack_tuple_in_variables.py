# Unpack a tuple into variables.

tup = (1, 2, 3, 4, 5)

a, b, *rest = tup

print("\nTuple: ", tup)
print(a, b, *rest)

print(*rest)
