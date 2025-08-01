#   Use filter() to remove empty strings from a list.

is_not_empty = lambda ele: ele.strip() != ""

lst = ["Hi,", "my", " ", "name", "is", " ", "Yash."]

print(f"\nList: ", lst)

filtered = list(filter(is_not_empty, lst))

print(f"Filtered list: {filtered}")
