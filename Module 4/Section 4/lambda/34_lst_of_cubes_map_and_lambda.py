#   Create a list of cubes using map and lambda

cube = lambda n: n * n * n

numbers = [num for num in range(1, 6)]

print(f"\nNumbers: ", numbers)
cubes = list(map(cube, numbers))
print("The cubes of these numbers is: ", *cubes)
