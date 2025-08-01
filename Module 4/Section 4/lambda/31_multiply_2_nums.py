# Write a lambda function to multiply two numbers.

multiply = lambda a, b: a * b

a, b = map(int, input("\nEnter 2 numbers: ").split())

print(f"The product of {a} and {b} is {multiply(a, b)}")
