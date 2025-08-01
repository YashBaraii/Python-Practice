# Use reduce() to compute factorial.

from functools import reduce

num = int(input("\nEnter the number: "))

# factorial = reduce(lambda x, y: x * y, [num for num in range(1, num + 1)])
# print(f"The factorial of {num} is: {factorial}")

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = reduce(lambda x, y: x * y, range(1, num + 1), 1)
    print(f"The factorial of {num} is: {factorial}")
