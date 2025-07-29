# Find the intersection of two sets.

st1 = {num for num in range(1, 6)}
st2 = {num for num in range(3, 9)}

print(f"\nSet 1: {st1} and Set 2: {st2}")

intersection = st1.intersection(st2)

print("\nIntersection: ", intersection)
