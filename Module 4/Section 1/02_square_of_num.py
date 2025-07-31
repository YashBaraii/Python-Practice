# Write a function that returns the square of a number.


def square(n):
    return n * n


num = int(input("\nEnter the number: "))

sq_num = square(num)
print(f"\nTh Sqaure of {num} is: {sq_num}")
