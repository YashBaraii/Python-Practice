# Create a histogram from a list of numbers using dictionaries


def histogram_dict(nums):
    num_counts = {}
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    return num_counts


numbers = [
    10,
    3,
    5,
    3,
    5,
    2,
    6,
    7,
    5,
    3,
    8,
    9,
    3,
    5,
    6,
    2,
    1,
    3,
    5,
    4,
    6,
    7,
    8,
    9,
    0,
    3,
    5,
    6,
    4,
    2,
    3,
    5,
    7,
    8,
    9,
    3,
    1,
    2,
    4,
    5,
    6,
    7,
    3,
    3,
    5,
    1,
    2,
    3,
    6,
    5,
    3,
    2,
    1,
    0,
    9,
    8,
    7,
    6,
    4,
    3,
]

print("\nNumbers: ", *numbers)
histogram = histogram_dict(numbers)

print("\nHistogram: ")
for num, count in histogram.items():
    print(
        f"{num} x {count} : {"⬜ " * count}",
    )
