# Find the sum of each row in a 2D list


def row_sums(lst):
    row_sum = []
    for row in lst:
        row_sum.append(sum(row))
    return row_sum[0], row_sum[1]


list_2d = [[1, 2], [3, 4]]

print("\nMatrix: ")
for row in list_2d:
    print(*row)

row1_sum, row2_sum = row_sums(list_2d)
print(f"\nThe sum of row1 is: {row1_sum} and row2 is: {row2_sum}.")
