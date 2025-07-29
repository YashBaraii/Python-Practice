# Given two lists, print common elements using sets.

lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]

print(f"\nList 1: {lst1} | List 2: {lst2}")

common = list(set(lst1) & set(lst2))
print("Common elements of both list: ", common)
