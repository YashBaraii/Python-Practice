# Check if all three conditions are True (using and).

is_divisible = lambda n: n % 1 == 0 and n % 2 == 0 and n % 3 == 0

num = int(input("Enter your num: "))

if is_divisible(num):
    print("Yes, it is divisible by 1, 2 and 3")
else:
    print("No, it is not divisible by 1, 2 and 3")
