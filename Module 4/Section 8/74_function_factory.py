# Function factory: make_multiplier(n) that returns a multiplier function.


def make_multiplier(n):
    def multiplier(x):
        return n * x

    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(15))
print(triple(5))
