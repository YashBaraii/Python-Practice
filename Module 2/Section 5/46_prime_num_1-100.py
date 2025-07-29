# Print all prime numbers between 1 to 100.
from math import sqrt


def prime_nums():
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")


print(f"\nThe Prime numbers between 1 and 100 are as follows: ")
prime_nums()
