# Check if a student has passed (marks ≥ 40 in each subject).

students = [
    {"id": 1, "username": "Yash", "maths": 90, "science": 85, "history": 97},
    {"id": 2, "username": "Ram", "maths": 70, "science": 89, "history": 93},
]

no_of_students = 2


def is_passed(id):
    for student in students:
        if id == student["id"]:
            return (
                student["maths"] >= 40
                and student["science"] >= 40
                and student["history"] >= 40
            )
    return False


username = input("Enter the name: ")


try:
    maths, science, history = map(
        float,
        input(
            "Enter the marks of all 3 subjects separated by comma (maths, science, history): "
        ).split(","),
    )
except ValueError:
    print("Invalid input for marks.")
    exit()


def display_all_students():
    print("\n--- Student Results ---")
    for student in students:
        status = "Passed" if is_passed(student) else "Failed"
        print(
            f"{student['username']} - Maths: {student['maths']}, Science: {student['science']}, History: {student['history']} → {status}"
        )


new_id = len(students) + 1
new_student = {
    "id": new_id,
    "username": username,
    "maths": maths,
    "science": science,
    "history": history,
}

students.append(new_student)
no_of_students += 1

if is_passed(no_of_students):
    print(f"\n{students[no_of_students-1]["username"]} is passed.")
else:
    print(f"\n{students[no_of_students-1]["username"]} is failed.")


display_all_students()
