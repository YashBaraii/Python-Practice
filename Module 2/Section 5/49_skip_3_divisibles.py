# Skip numbers divisible by 3 using continue.


def print_nums(n):
    print(" ".join(str(num) for num in range(1, n + 1) if num % 3 != 0))


def print_nums2(n):
    for num in range(1, n + 1):
        if num % 3 == 0:
            continue
        print(num, end=" ")


num = int(input("Enter the number: "))
print_nums2(num)
