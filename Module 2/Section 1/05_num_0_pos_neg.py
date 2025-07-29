# Determine if the entered number is zero, positive, or negative.


def check(num):
    if num < 0:
        print(f"{num} is negative number.")
    elif num > 0:
        print(f"{num} is positive number.")
    else:
        print(f"{num} is zero")


num = int(input("Enter the number: "))
check(num)
