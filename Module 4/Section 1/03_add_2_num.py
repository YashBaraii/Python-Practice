# Create a function that adds two numbers.


def add(a, b):
    return a + b


a, b = map(float, (input("\nEnter two numbers: ").split()))

print(f"\nThe addition of {a} and {b} is {add(a, b)}")
