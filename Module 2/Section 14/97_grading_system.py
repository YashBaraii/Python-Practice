# Grading System: Input marks for 5 subjects → Calculate percentage → Grade.

cal_percentage = lambda lst: (sum(lst) / (len(lst) * 100)) * 100


def find_grade(p):
    if p >= 90:
        return "A"
    elif p >= 80:
        return "B"
    elif p >= 70:
        return "C"
    elif p >= 60:
        return "D"
    elif p >= 50:
        return "E"
    elif p >= 40:
        return "F"
    else:
        return "Fail"


marks_list = []

print("\n----- Grading System -----\n")

for i in range(5):
    marks = float(input(f"Enter your marks of subject {i+1}: "))
    marks_list.append(marks)

percentage = cal_percentage(marks_list)
print(f"\nYour grade is {find_grade(percentage)}. And your percentage is: {percentage}")
