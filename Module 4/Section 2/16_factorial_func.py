# Create a function that returns the factorial of a number.


def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


num = int(input("\nEnter the number: "))

print(f"The factorial of {num} is: {factorial(num)}")
