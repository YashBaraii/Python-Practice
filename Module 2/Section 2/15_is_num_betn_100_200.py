# Check if a number is between 100 and 200.

is_between = lambda num: 100 <= num <= 200

num = int(input("Enter the number: "))

if is_between(num):
    print(f"\n{num} is between 100 and 200.")
else:
    print(f"\n{num} is not between 100 and 200.")
