# Check if a number is divisible by 2 or 3 but not 5.

is_divisible = lambda n: (n % 2 == 0 or n % 3 == 0) and (n % 5 != 0)
num = int(input("Enter your num: "))

if is_divisible(num):
    print("Yes, it is divisible by 2 or 3 but not 5")
else:
    print("No, it is not divisible by 2 or 3 but by 5")
