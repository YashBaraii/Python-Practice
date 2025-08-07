#   Use map() with a list of functions on a single value.

square = lambda n: n * n
cube = lambda n: n * n * n

n = int(input("\nEnter the number: "))
results = list(map(lambda f: f(n), [square, cube]))

print(f"The Square and Cube of {n} are: (", *results, ") respectively.")
