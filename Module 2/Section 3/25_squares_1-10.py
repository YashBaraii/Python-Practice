# Print squares of numbers 1 to 10.

print("\nSquares of numbers 1 to 10: ")
print(*(num * num for num in range(1, 11)), sep=" ")
