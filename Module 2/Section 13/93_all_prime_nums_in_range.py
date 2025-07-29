# Find all prime numbers in a range given by the user.

from math import isqrt


def is_prime(n):
    for num in range(2, isqrt(n) + 1):
        if n % num == 0:
            return False
    return True


def prime_nums(st, en):
    if st == 0 or st == 1:
        st = 2
    if st < 0:
        return None
    nums = []
    for num in range(st, en + 1):
        if is_prime(num):
            nums.append(num)
    return nums


st, en = map(int, input("\nEnter the start and end range (x-x): ").split(","))


nums = prime_nums(st, en)

if nums is not None:
    print(f"\nAll the prime numbers from {st} to {en} are as follows: \n{nums}")
else:
    print("Prime numbers can't be negative, please enter valid range!")
