# Extract digits from a 3-digit number and print the sum.


def sum_digits(num):
    if len(str(num)) != 3:
        raise ValueError("Input should be a 3-digit number")

    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10

    return hundreds + tens + ones


num = int(input("\nEnter the number: "))
print(f"The sum of the digits is: {sum_digits(num)}")
