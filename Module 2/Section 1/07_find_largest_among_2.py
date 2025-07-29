# Determine the largest of two numbers.

find_largest = lambda a, b: a if a > b else b

num1, num2 = map(int, input("Enter two numbers separated by comma: ").split(","))

result = find_largest(num1, num2)

print(f"\nThe largest number is: {result}")
