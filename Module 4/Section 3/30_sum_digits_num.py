# Function that returns the sum of digits of a number.


def sum_of_digits(num):
    return sum([int(d) for d in str(num)])


num = int(input("\nEnter the number: "))

print(f"The of sum of digits of number {num} is: {sum_of_digits(num)}")
