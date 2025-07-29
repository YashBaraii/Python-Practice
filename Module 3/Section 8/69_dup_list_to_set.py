# Convert a list with duplicates to a set.

lst = [1, 2, 3, 4, 5, 1, 2, 3]

print("\nList with duplicates: ", *lst)
lst = list(set(lst))
print("\nList without duplicates by help of set: ", *lst)
