# Find the GCD of two numbers.


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


num1, num2 = map(int, input("Enter 2 numbers separated by comma: ").split(","))

print(f"The GCD is: {find_gcd(num1, num2)}")
