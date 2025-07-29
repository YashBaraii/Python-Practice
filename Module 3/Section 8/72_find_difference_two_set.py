# Find the difference between two sets.

st1 = {num for num in range(1, 6)}
st2 = {num for num in range(3, 9)}

print(f"\nSet 1: {st1} and Set 2: {st2}")

st1_diff = st1.difference(st2)
st2_diff = st2.difference(st1)

print("\nSet 1 difference: ", st1_diff)
print("\nSet 2 difference: ", st2_diff)
