# Remove all duplicates from a list.


lst = [1, 3, 2, 1, 4, 5, 3]
print(f"\nOriginal list: ", lst)

lst = list(set(lst))

print(f"List after removing duplicates: {lst}")
