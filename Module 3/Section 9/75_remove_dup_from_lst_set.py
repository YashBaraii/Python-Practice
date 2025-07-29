# Remove duplicates from a list using a set.

lst = [1, 2, 3, 4, 3, 4, 5]

print("\nList: ", lst)

lst = list(set(lst))
print("List after removing duplicates by converting it to set: ", lst)
