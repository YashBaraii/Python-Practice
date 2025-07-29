# Write a program to swap the first and last digits of a 3-digit number.


def swap1(num):
    st_num = str(num)
    if len(st_num) != 3:
        raise ValueError("Input must be a 3-digit number")

    first_digit = st_num[0]
    last_digit = st_num[-1]
    swapped_digit = int(last_digit + st_num[1] + first_digit)
    return swapped_digit


def swap2(num):
    if num < 100 or num > 999:
        raise ValueError("Input must be a 3-digit number")

    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10

    swapped = units * 100 + tens * 10 + hundreds
    return swapped


num = int(input("Enter the number: "))

print(swap1(num))
print(swap2(num))
