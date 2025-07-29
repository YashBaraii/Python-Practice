# Determine letter grades from a percentage (A, B, C...).

find_grade = lambda p: (
    "A"
    if p >= 90
    else (
        "B"
        if p >= 80
        else "C" if p >= 70 else "D" if p >= 60 else "E" if p >= 50 else "F"
    )
)

percentage = float(input("Enter the percentage: "))

grade = find_grade(percentage)

print(f"\nYour grade is: {grade}")
