# Check if a number is a palindrome.


def is_palindrome(num):
    i = len(str(abs(num))) - 1
    reverse = []
    while i >= 0:
        reverse.append(str(abs(num))[i])
        i -= 1
    return abs(num) == int("".join(ch for ch in reverse))


num = int(input("\nEnter the number: "))


if is_palindrome(num):
    print("Yes, It is a palindrome.")
else:
    print("No, It is not a palindrome.")
