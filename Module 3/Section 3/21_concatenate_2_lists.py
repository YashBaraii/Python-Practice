# Concatenate two lists.

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

print(f"\nFirst list: {lst1} and Second list: {lst2}")

lst1.extend(lst2)
concatenate = lst1 + lst2
concatenate2 = list(set(lst1).union(set(lst2)))
concatenate2 = list(set(lst1) | set(lst2))

# print("The contenated version of both the lists is: ", concatenate)
print("The contenated version of both the lists is: ", lst1)
