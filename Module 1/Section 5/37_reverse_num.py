# Reverse the digits of an integer (e.g., 123 → 321).


def reverse(num):
    lst_num = list(str(num))
    reversed = lst_num[::-1]
    return int("".join([i for i in reversed]))


reverse2 = lambda num: int(str(num)[::-1])


num = int(input("Enter the number: "))
print("\nIts reversed form is: ", reverse2(num))
