# Classify a triangle by its sides: Equilateral, Isosceles, or Scalene.


def classify_triangle(a, b, c):
    if a == b == c:
        print(f"\nIt is the Equilateral Triangle.")
    elif (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
        print(f"\nIt is the Isoscales Triangle.")
    else:
        print(f"\nIt is the Scalene Triangle.")


a, b, c = map(
    float, input("Enter the 3 sides of triangle separated by comma: ").split(",")
)

classify_triangle(a, b, c)
