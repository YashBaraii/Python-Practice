# Take two integers and print which one is divisible by the other.


def find_divisible_one(a, b):
    if b != 0 and a % b == 0:
        return a
    elif a != 0 and b % a == 0:
        return b
    else:
        return None


num1, num2 = map(int, input("\nEnter two numbers separated by comma: ").split(","))

result = find_divisible_one(num1, num2)

if result is not None:
    print(f"{result} is divisible by the other.")
else:
    print("Neither number is divisible by the other.")
