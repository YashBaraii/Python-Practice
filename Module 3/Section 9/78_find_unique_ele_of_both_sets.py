# Find elements that are in either of two sets but not both.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print(f"\nSet 1: {set1} | Set 2: {set2}")

uniques = set(list(set1.difference(set2)) + list(set2.difference(set1)))
print(
    f"The elements that are in either of two sets but not both are as follows: \n{uniques}"
)
