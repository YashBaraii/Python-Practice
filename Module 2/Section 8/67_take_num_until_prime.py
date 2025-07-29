# Ask for a number and keep asking until a prime is entered

from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for num in range(2, isqrt(n) + 1):
        if n % num == 0:
            return False
    return True


while True:
    num = int(input("\nEnter the number: "))

    if is_prime(num):
        print("\nYes, now you have entered prime number. ")
        break
