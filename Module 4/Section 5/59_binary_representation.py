#   Recursive function to compute binary representation of a number.


def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)


num = int(input("\nEnter the number: "))
binary = to_binary(num)
print(f"Binary of {num} is: {binary}")
