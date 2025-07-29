# Count how many items in a list are greater than 50.

lst = [3, 51, 40, 88, 66]

print("List: ", lst)

count = lambda lst: sum([1 for item in lst if item > 50])

print(f"There are total {count(lst)} items that are greater than 50")
