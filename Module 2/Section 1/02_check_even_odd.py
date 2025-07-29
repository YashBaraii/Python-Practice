# Input a number and determine if it's even or odd.

is_even = lambda num: num % 2 == 0

num = int(input("Enter the number: "))

if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
