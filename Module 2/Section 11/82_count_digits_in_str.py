# Count how many digits are in a string.


def count_digits(st):
    count = 0
    for ch in st:
        if ch.isdigit():
            count += 1

    return count


st = input("\nEnter something: ")
print(f"Total no of digits in this string is: {count_digits(st)}")
