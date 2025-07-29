# Print numbers 1 to 10

print(" ".join(str(num) for num in range(1, 11)))

print(*(num for num in range(1, 11)), sep=" ")
