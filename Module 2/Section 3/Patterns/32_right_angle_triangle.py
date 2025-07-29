# Print a right-angle triangle of stars.


def right_angle_triangle(n):
    for i in range(n):
        for _ in range(i + 1):
            print("* ", end=" ")
        print()


n = int(input("\nEnter the number: "))

print("\nRight angle triangle of stars: ")
right_angle_triangle(n)
