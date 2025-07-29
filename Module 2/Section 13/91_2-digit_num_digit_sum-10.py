# Find all 2-digit numbers where sum of digits = 10.


def find_nums():
    nums = []
    for num in range(10, 100):
        tens = (num // 10) % 10
        ones = num % 10
        if tens + ones == 10:
            nums.append(num)
    return nums


find_nums2 = lambda: [
    num for num in range(10, 100) if (num % 10 + ((num // 10) % 10)) == 10
]

digit_sum_10_nums = find_nums2()

print(
    f"All the numbers where sum of digits is 10 are as follows: \n{digit_sum_10_nums}"
)
