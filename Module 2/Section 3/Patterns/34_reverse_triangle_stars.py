# Print a reverse triangle of stars.


def reverse_triangle(n):
    x = 0
    for i in range(n, 0, -1):
        spaces = " " * x
        stars = "* " * i
        x += 1
        print(spaces + stars)


n = int(input("\nEnter the number: "))

print("\nReverse Triangle of stars: ")
reverse_triangle(n)
