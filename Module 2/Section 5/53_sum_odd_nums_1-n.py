# Print the sum of all odd numbers between 1 and N.


def sum1(n):
    sum = 0
    for num in range(1, n + 1, 2):
        sum += num

    return sum


sum2 = lambda n: sum(range(1, n + 1, 2))

num = int(input("Enter the number: "))
print(f"\nThe sum of all odd numbers between 1 and {num} is: {sum2(num)}")
