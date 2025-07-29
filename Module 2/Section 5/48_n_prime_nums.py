# Print the first N prime numbers.

from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for num in range(2, int(sqrt(n)) + 1):
        if n % num == 0:
            return False
    return True


def first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1


num = int(input("Enter the number: "))
print(f"First {num}th prime numbers: ")
first_n_primes(num)
