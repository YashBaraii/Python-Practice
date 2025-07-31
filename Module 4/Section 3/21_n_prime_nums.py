# Function to convert Celsius to Fahrenheit.

from math import isqrt


def is_prime(num):
    for n in range(2, isqrt(num) + 1):
        if num % n == 0:
            return False

    return True


def n_prime_nums(n):
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=" ")


num = int(input("\nEnter the number: "))
print(f"\nAll Prime numbers till {num} are as follows: ")
n_prime_nums(num)
