# Find the square and cube of a number.

square = lambda n: n * n
cube = lambda n: n * n * n

num = int(input("\nEnter the number: "))
print(f"\nIts square is: {square(num)}")
print(f"Its cube is: {cube(num)}")
