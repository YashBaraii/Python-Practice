# Take input of 2 numbers and print their sum, difference, product, and division.

a, b = map(int, input("Enter two numbers separated by comma: ").split(","))

print(f"The sum of {a} and {b} is: {a + b}")
print(f"The diff of {a} and {b} is: {a - b}")
print(f"The prod of {a} and {b} is: {a * b}")

div = a / b if b != 0 else None
if div is not None:
    print(f"The div of {a} and {b} is: {div}")
else:
    print("Err: Division by zero is not allowed !")
