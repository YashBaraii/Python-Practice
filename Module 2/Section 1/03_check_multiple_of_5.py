# Check if a number is a multiple of 5.

is_multiple = lambda num: num % 5 == 0

num = int(input("Enter the number: "))

if is_multiple(num):
    print(f"{num} is the multiple of 5")
else:
    print(f"{num} is not the multiple of 5")
