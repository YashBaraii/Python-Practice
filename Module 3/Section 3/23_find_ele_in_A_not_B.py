# Find elements that are in list A but not in B.

lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6]

# lst1_uniques = list(set(lst1) - set(lst2))
lst1_uniques = list(set(lst1).difference(set(lst2)))

print(f"\nFirst list: {lst1} and Second list: {lst2}")

print("The elements that are in list 1 but not in list 2 are: ", lst1_uniques)
