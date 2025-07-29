# Create a matrix (list of lists) and print it.

lst_of_lsts = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\nList of lists: ")
for list in lst_of_lsts:
    print(*list)
