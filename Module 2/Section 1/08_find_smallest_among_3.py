# Find the smallest of three numbers.

find_smallest = lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c

num1, num2, num3 = map(int, input("Enter 3 numbers separated by comma: ").split(","))

result = find_smallest(num1, num2, num3)

print(f"\nThe Smallest numbers is: {result}")
