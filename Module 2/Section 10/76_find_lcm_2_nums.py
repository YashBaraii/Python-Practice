# Find the LCM of two numbers.


def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_lcm(a, b):
    return abs(a * b) // compute_gcd(a, b)


num1, num2 = map(int, input("\nEnter 2 numbers separated by comma: ").split(","))
print(f"The LCM is: {find_lcm(num1, num2)}")
