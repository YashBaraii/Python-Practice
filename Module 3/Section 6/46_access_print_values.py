# Access and print a value using its key.

Student = {"name": "Yash", "age": 17, "grade": "A"}

print("\nStudent values: ")
print(f"Name: {Student.get("name")}")
print(f"Age: {Student.get("age")}")
print(f"Grade: {Student.get("grade")}")
