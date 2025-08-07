# Recursive function to find factorial of a number


def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


num = int(input("\nEnter the number: "))

print(f"The Factorial of {num} is: {factorial(num)}")
