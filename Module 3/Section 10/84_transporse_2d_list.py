# Create a matrix (list of lists) and print it.

matrix = [[1, 2], [3, 4]]

print("\nMatrix: ")
for row in matrix:
    print(*row)

transporse = [row for row in matrix]

transporse[0][1], transporse[1][0] = transporse[1][0], transporse[0][1]

print("\nTransporse 2d matrix: ")
for row in transporse:
    print(*row)
