#   Recursive function to compute power x^n.


def compute(x, n):
    if n == 0:
        return 1
    return x * compute(x, n - 1)


x, n = map(float, input("\nEnter the x and n (x^n): ").split("^"))

print(f"The Result of {x}^ {n} is: {compute(x, n)}")
