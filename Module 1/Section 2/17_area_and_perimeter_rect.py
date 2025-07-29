# Calculate area and perimeter of a rectangle.

l, w = map(
    int, input("Enter Length and Width of Rectangle separated by comma: ").split(",")
)

area = l * w
perimeter = 2 * (l + w)

print(f"The Area of Rectangle is: {area}")
print(f"The Perimeter of Rectangle is: {perimeter}")
