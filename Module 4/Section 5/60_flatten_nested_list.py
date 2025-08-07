# Recursive function to flatten a nested list.


def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # Recursive case
        else:
            result.append(item)  # Base case
    return result


lst = [[1, 2, [3]], [4, 5], 6]
flat = flatten(lst)
print(flat)
