# Print all 3-digit Armstrong numbers.

from math import pow


def find_nums():
    nums = []
    for num in range(100, 1000):
        h = num // 100
        t = (num // 10) % 10
        o = num % 10
        if pow(h, 3) + pow(t, 3) + pow(o, 3) == num:
            nums.append(num)

    return nums


nums = find_nums()
print(f"\nAll the 3-digits Armstrong numbers are as follows: \n{nums}")
