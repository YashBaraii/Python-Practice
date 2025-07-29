# Check if one set is a subset of another.

st1 = {1, 2, 3, 4, 5}
st2 = {1, 2, 3}

print(f"\nSet 1: {st1} and Set 2: {st2}")

if st1.issubset(st2):
    print("Yes, st1 is subset of st2")
elif st2.issubset(st1):
    print("Yes, st2 is subset of st1")
else:
    print("No, no-one is subset of another")
