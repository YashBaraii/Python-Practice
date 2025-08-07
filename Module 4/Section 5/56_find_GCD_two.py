# Recursive function to find GCD of two numbers


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input("\nEnter two numbers separated by comma: ").split())

print("The GCD is: ", gcd(a, b))
