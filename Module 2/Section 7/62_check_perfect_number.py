# Check if a number is a perfect number (sum of divisors equals the number).


def is_perfect_number(n):
    divisors = []
    for num in range(1, n):
        if n % num == 0:
            divisors.append(num)
    return sum(divisors) == n


num = int(input("Enter the number: "))


if is_perfect_number(num):
    print("\nYes, it is perfect number.")
else:
    print("\nNo. it is not perfect number.")
