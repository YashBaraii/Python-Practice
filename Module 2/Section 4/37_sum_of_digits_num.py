# Print sum of digits of a number.


def sum_of_digits(n):
    st_n = str(abs(n))
    sum = 0
    i = 0
    while i < len(st_n):
        sum += int(st_n[i])
        i += 1
    return sum


sum_of_digits2 = lambda n: sum(int(d) for d in str(abs(n)))


num = int(input("Enter the number: "))
print(f"The sum of its digits is: {sum_of_digits(num)}")
