# Function that returns the first n Fibonacci numbers.


def fibo_series_n(n):
    fibo = [0, 1]
    if n < 0:
        return ["Err: Number", "can't", "be", "negative !"]
    if n <= 2:
        return fibo
    for _ in range(n - 2):
        fibo.append(sum(fibo[-2:]))
    return fibo


num = int(input("\nEnter the number: "))

first_n_fibo = fibo_series_n(num)
print(f"The first {num} fibonacci numbers are as follows: \n", *first_n_fibo)
