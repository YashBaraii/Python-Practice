# Create a program to check whether the last digit of a number is even or odd.


def is_even1(num):
    last_digit = num % 10
    return last_digit & 1 == 0


is_even2 = lambda num: (num % 10) & 1 == 0


num = int(input("\nEnter the number: "))
if is_even2(num):
    print(f"Last digit ({num % 10}) is even")
else:
    print(f"Last digit ({num % 10}) is odd")
