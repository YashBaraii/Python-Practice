# Use lambda to check if a number is even.

is_even = lambda n: n & 1 == 0

num = int(input("\nEnter the number: "))

if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
