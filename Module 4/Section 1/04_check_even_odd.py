# Write a function to check if a number is even.


def is_even(num):
    return num & 1 != 0


num = int(input("\nEnter the number: "))

if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
