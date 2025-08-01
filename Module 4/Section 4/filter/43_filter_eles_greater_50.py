# Use filter() to get elements greater than 50.

is_greater_than_50 = lambda n: n > 50

lst = [1, 53, 20, 38, 76, 88]
print(f"\nList: ", lst)

greater_than_50_lst = list(filter(is_greater_than_50, lst))

print(f"These are the elements who are greater than 50: {greater_than_50_lst}")
