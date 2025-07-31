# Function to return the maximum of two numbers.


def max_num(a, b):
    return max(a, b)


a, b = map(float, input("\nEnter two number: ").split())

print(f"The Maximum is: {max_num(a, b)}")
