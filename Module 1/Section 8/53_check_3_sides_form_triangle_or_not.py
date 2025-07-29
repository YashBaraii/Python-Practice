# Check if three sides form a triangle (Triangle Inequality Theorem).


def check_triangle(s1, s2, s3):
    return (s1 + s2) > s3 and (s1 + s3) > s2 and (s2 + s3) > s1


a, b, c = map(int, input("\nEnter 3 sides of triangle separated by comma: ").split(","))

if check_triangle(a, b, c):
    print("Triangle can be form")
else:
    print("Triangle can't be form")
