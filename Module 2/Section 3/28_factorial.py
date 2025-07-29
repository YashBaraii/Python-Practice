# Print the factorial of a number.


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def factorial2(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial2(n - 1)


factorial3 = lambda n: 1 if n == 0 or n == 1 else n * factorial3(n - 1)

num = int(input("Enter the number: "))

print(f"The factorial of {num} is: {factorial3(num)}")
