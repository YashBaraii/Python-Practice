# Count digits in a number.


def digit_count(n):
    i = 0
    while i < len(str(abs(n))):
        i += 1
    return i


digit_count2 = lambda n: len(str(abs(n)))

num = int(input("Enter the number: "))
print(f"Its digit count is: {digit_count(num)}")
