# Function that returns another function which multiplies input by n.


def multiplier(n):
    def inner(x):
        return x * n

    return inner


double = multiplier(2)
triple = multiplier(3)

print(double(5))  # 10
print(triple(4))  # 12
