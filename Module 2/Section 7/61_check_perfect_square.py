# Check if a number is a perfect square.

from math import sqrt


def is_perfect_square(n):
    if n < 0:
        return False
    root = sqrt(n)
    return root * root == n


num = int(input("Enter your num: "))

if is_perfect_square(num):
    print("Yes, it is perfect square.")
else:
    print("No, it is not perfect square.")
