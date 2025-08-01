#   Function that finds common elements between two lists.


def find_commons(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))


lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]

print(f"\nList 1: {lst1} and List 2: {lst2}")
print(f"The common elements are: {find_commons(lst1, lst2)}")
