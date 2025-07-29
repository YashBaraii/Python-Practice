# Check if a number is odd and greater than 100.

check = lambda num: num & 1 == 1 and num > 100

num = int(input("Enter the number: "))

if check(num):
    print(f"\n{num} is odd and greater than 100.")
else:
    print(f"\n{num} is not odd and greater than 100.")
