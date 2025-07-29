# Take 3 inputs and print the greatest number.

find_greatest = lambda a, b, c: a if a > b and a > c else b if b > c and b > a else c

num1, num2, num3 = map(int, input("Enter 3 numbers separated by comma: ").split(","))

result = find_greatest(num1, num2, num3)

print(f"\n{result} is greatest number among those 3 numbers.")
