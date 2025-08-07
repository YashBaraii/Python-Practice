#   Recursive function to print numbers from n to 1.


def print_nums(n):
    if n == 0:
        return
    print(n, end=" ")
    return print_nums(n - 1)


num = int(input("\nEnter the number: "))
print("The numbers are: \n")
print_nums(num)
