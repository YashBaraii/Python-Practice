# Group names by their first letter using a dictionary.


def group_students(students):
    grouped_students = {}
    for student in students:
        first_letter = student["name"][0].upper()
        if first_letter not in grouped_students:
            grouped_students[first_letter] = []
        grouped_students[first_letter].append(student)

    return grouped_students


students = [
    {"id": 1, "name": "Aatmaram Bhide", "age": 17, "grade": "10", "gender": "Male"},
    {"id": 2, "name": "Arohi Sharma", "age": 15, "grade": "8", "gender": "Female"},
    {"id": 3, "name": "Suhani Shah", "age": 14, "grade": "7", "gender": "Female"},
    {"id": 4, "name": "Krish Bhatt", "age": 16, "grade": "9", "gender": "Male"},
    {"id": 5, "name": "Arjun Raj", "age": 17, "grade": "10", "gender": "Male"},
]

print("\nClass of students: ")
for student in students:
    print(
        f"{student["id"]}. {student["name"]} - Grade {student["grade"]} - Age {student["age"]}"
    )

print()

grouped_students = group_students(students)

print("\nGrouped by first letter of name: ")
for key in sorted(grouped_students.keys()):
    print(f"{key}: {[s["name"] for s in grouped_students[key]]}")
