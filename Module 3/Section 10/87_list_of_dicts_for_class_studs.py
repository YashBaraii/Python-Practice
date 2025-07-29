# Create a list of dictionaries representing a class of students

students = [
    {"id": 1, "name": "xyz abc", "age": 17, "grade": "10", "gender": "Male"},
    {"id": 2, "name": "abc abc", "age": 15, "grade": "8", "gender": "Female"},
]

print("\nClass of students: ")
for student in students:
    for key, value in student.items():
        print(f"{key}: {value}")
    print()
