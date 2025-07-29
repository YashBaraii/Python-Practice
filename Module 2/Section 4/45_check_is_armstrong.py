# Check if a number is an Armstrong number.

from math import pow


def is_armstrong(num):
    sum_value = int(sum(pow(int(n), len(str(abs(num)))) for n in str(abs(num))))
    return sum_value == num


num = int(input("\nEnter the number: "))


if is_armstrong(num):
    print("Yes, It is a Armstrong number.")
else:
    print("No, It is not a Armstrong number.")
