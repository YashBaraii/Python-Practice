# Print Fibonacci sequence up to N terms.


def fibonacci(n):
    if n < 0:
        print("Please enter a positibe integer.")
        return

    elif n == 1:
        print(f"\nThe Fibonacci sequence upto 1st term is: 0")
        return

    first, second = 0, 1
    i = 0
    print(f"\nThe Fibonacci sequence upto {n}th term is: {first}, {second},", end=" ")
    while i < n - 2:
        punctuation = ". " if i == n - 3 else ", "
        next = first + second
        print(f"{next}", end=punctuation)
        first, second = second, next
        i += 1


num = int(input("Enter the number: "))

fibonacci(num)
