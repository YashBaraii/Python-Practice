# Print a square of stars (5x5).


def square_of_stars(n):
    for _ in range(n):
        for _ in range(n):
            print("* ", end=" ")
        print()


n = int(input("\nEnter the number: "))

print("\nSquare of stars: ")
square_of_stars(n)
