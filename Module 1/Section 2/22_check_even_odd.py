# Input a number, check if it’s even or odd.


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


is_odd = lambda n: True if n % 2 != 0 else False

num = int(input("Enter the number: "))

if is_odd(num):
    print(f"\n{num} is odd")
else:
    print(f"\n{num} is even")
