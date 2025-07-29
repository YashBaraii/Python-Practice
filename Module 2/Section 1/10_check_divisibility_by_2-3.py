# Check if a number is divisible by 2 and 3.

is_divisible = lambda num: num % 2 == 0 and num % 3 == 0

num = int(input("Enter the number: "))

if is_divisible(num):
    print(f"\n{num} is divisible by both 2 and 3.")
else:
    print(f"\n{num} is not divisible by both 2 and 3.")
