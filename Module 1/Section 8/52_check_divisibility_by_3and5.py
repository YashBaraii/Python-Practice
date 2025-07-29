# Input a number and print True if it's divisible by both 3 and 5.


def check_divisibility(num):
    if num % 3 == 0 and num % 5 == 0:
        return True
    return False

    # return num % 3 == 0 and num % 5 == 0


check_divisibility2 = lambda num: num % 3 == 0 and num % 5 == 0

num = int(input("Enter the number: "))

if check_divisibility(num):
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is not divisible by either 3 or 5")
