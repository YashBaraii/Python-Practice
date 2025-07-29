# Calculate the digit sum of any number.


def digit_sum(num):
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum += last_digit
        num //= 10
    return sum


num = int(input("\nEnter the number: "))
print(f"Its digit sum is: {digit_sum (num)}")
