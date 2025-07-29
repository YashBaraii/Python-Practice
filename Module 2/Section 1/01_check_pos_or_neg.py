# Check if a number is positive or negative.

is_positive = lambda num: num > 0

num = int(input("Enter the number: "))
if is_positive(num):
    print(f"{num} is a positive number.")
else:
    print(f"{num} is a negative number.")
