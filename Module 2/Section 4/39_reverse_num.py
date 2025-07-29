# Reverse a number.


def reverse(n):
    i = len(str(abs(n))) - 1
    reversed = []
    sign = -1 if n < 0 else i
    while i >= 0:
        reversed.append(str(abs(n))[i])
        i -= 1
    return int("".join(ch for ch in reversed)) * sign


num = int(input("Enter the number: "))
print(f"Its reversed form is: {reverse(num)}")
