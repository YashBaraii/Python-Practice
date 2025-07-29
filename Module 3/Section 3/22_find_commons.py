# Find the common elements between two lists.

lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6]

commons = list(set(lst1) & set(lst2))
commons = set(lst1).intersection(set(lst2))

print(f"\nFirst list: {lst1} and Second list: {lst2}")

print("The common elements of both the lists is: ", commons)
