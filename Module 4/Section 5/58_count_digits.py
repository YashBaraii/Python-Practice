# Recursive function to count digits in a number.


def count_digits(num):
    if num <= 0:
        return 0
    return 1 + count_digits(num // 10)


num = int(input("\nEnter the number: "))

print(f"The count of the digts is: {count_digits(num)}")
