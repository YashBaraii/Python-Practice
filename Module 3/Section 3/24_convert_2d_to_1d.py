# Flatten a 2D list into a 1D list.

lst_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst = sum(lst_2d, [])
lst2 = [item for sublist in lst_2d for item in sublist]

print("\n2d list: \n", lst_2d)

print(lst)
print(lst2)
