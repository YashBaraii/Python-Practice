# Sort the list of students by age.

students = [
    {"id": 1, "name": "Ram Chaurasiya", "age": 17, "grade": "10", "gender": "Male"},
    {"id": 2, "name": "Ishani Sharma", "age": 15, "grade": "8", "gender": "Female"},
    {"id": 3, "name": "Suhani Shah", "age": 14, "grade": "7", "gender": "Female"},
    {"id": 4, "name": "Krish Bhatt", "age": 16, "grade": "9", "gender": "Male"},
    {"id": 5, "name": "Arjun Raj", "age": 17, "grade": "10", "gender": "Male"},
]

print("\nClass of students: ")
for student in students:
    print(
        f"{student["id"]}. {student["name"]} - Grade {student["grade"]} - Age {student["age"]}"
    )

sorted_students = sorted(students, key=lambda st: st["age"])

print("\nClass of students in sort by age: ")
for student in sorted_students:
    print(
        f"{student["id"]}. {student["name"]} - Grade {student["grade"]} - Age {student["age"]}"
    )
