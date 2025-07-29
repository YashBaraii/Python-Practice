# Find the factorial using while loop.


def factorial(n):
    i = 1
    fact = 1
    while i < n + 1:
        fact *= i
        i += 1
    return fact


num = int(input("Enter the number: "))

print(f"\nThe factorial of {num} is: {factorial(num)}")
