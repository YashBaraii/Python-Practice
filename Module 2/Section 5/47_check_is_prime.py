# Check if a number is prime.

from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Enter the number: "))

if is_prime(num):
    print(f"\n{num} is Prime number.")
else:
    print(f"\n{num} is not Prime number.")
