# Find the union of two sets.

st1 = {num for num in range(1, 6)}
st2 = {num for num in range(6, 11)}

print(f"\nSet 1: {st1} and Set 2: {st2}")

union = st1.union(st2)
print("Union of both sets: ", union)
