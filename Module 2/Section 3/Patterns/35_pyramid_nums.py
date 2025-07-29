# Print a pyramid of numbers.


# def nums_pyramid(n):
#     for i in range(1, n + 1):
#         spaces = " " * (n - i)
#         numbers = " ".join(str(x) for x in range(1, i + 1))
#         print(spaces, numbers)


# def nums_pyramid2(n):
#     num = 1
#     for i in range(1, n + 1):
#         spaces = " " * (n - i)
#         row_numbers = " ".join(str(num + j) for j in range(i))
#         print(spaces + row_numbers)
#         num += i


def nums_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        numbers = " ".join(str(num) for num in range(1, i + 1))
        print(spaces + numbers)


def nums_pyramid2(n):
    num = 1
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        row_numbers = " ".join(str(num + j) for j in range(i))
        print(spaces + row_numbers)
        num += i


n = int(input("\nEnter the number: "))

print("\nPyramid of numbers: ")
nums_pyramid2(n)
