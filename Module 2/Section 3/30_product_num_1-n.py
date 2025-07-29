# Print the product of numbers from 1 to N

from math import prod


def product(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


product2 = lambda n: 1 if n == 0 or n == 1 else n * product2(n - 1)

product3 = lambda n: None if n < 0 else 0 if n == 0 else prod(range(1, n + 1))

num = int(input("Enter the number: "))

print(f"\nThe Product of numbers till {num} is: {product3(num)}")
