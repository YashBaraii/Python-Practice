# Recursive function to compute nth Fibonacci number.


def fibo_num(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_num(n - 1) + fibo_num(n - 2)


n = int(input("\nEnter the nth term for fibonacci number: "))
print(f"The {n}th fibonacci number is: {fibo_num(n)}")
