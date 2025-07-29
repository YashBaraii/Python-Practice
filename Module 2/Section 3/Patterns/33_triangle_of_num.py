# Print a triangle of numbers (1 22 333 ...).


def num_triangle(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        numbers = f"{i} " * i
        print(spaces + numbers)


n = int(input("\nEnter the number: "))

print("\nTriangle of nums: ")
num_triangle(n)
