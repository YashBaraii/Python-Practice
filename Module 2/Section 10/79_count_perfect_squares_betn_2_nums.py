# Count how many perfect squares exist between two numbers.

from math import isqrt


def is_perfect_square(num):
    root = isqrt(num)
    return root * root == num


def count_perfect_squares(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_perfect_square(num):
            count += 1
    return count


def count_perfect_squares2(start, end):
    return isqrt(end) - isqrt(start - 1)


num1, num2 = map(int, input("Enter 2 numbers separated by comma: ").split(","))

print(
    f"The total number of perfect square that are between {num1} and {num2} is: {count_perfect_squares2(num1, num2)}"
)
