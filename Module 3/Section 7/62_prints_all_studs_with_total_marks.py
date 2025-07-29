# Print all students and their total marks.

students = [
    {"id": 1, "name": "s1", "sub1": 70, "sub2": 76, "sub3": 79},
    {"id": 2, "name": "s2", "sub1": 96, "sub2": 60, "sub3": 80},
]


for student in students:
    print(
        f"{student["id"]}. {student["name"]} - Total Marks: {student["sub1"] + student["sub2"] + student["sub3"]}"
    )
