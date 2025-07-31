# Function that removes all duplicates from a list.


def remove_dups(lst):
    return list(set(lst))


lst = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7]

print(f"\nOriginal List: ", *lst)
lst = remove_dups(lst)

print(f"The List after removing duplicates: ", *lst)
