#   Use map() to add two lists element-wise

add = lambda a, b: a + b

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

print(f"\nList 1: {lst1} and List 2: {lst2}")

lst = list(map(add, lst1, lst2))

print("Result:", lst)
