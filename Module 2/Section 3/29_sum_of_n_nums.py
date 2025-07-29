# Print the sum of numbers from 1 to N.


def sum_of_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def sum_of_n2(n):
    return sum(range(1, n + 1))


sum_of_n3 = lambda n: sum(range(1, n + 1))


def sum_of_n4(n):
    return n * (n + 1) // 2


sum_of_n5 = lambda n: n * (n + 1) // 2

num = int(input("Enter the number: "))
print(f"The sum of numbers till {num} is: {sum_of_n5(num)}")
