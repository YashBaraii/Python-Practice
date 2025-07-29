# Update the age of the student.

Student = {"name": "Yash", "age": 17, "grade": "A"}

print("\nStudent dict: ")
print(f"Name: {Student.get("name")}")
print(f"Age: {Student.get("age")}")
print(f"Grade: {Student.get("grade")}")

age = int(input("\nEnter the age: "))
Student["age"] = age

print(f"Student's age is now updated to {age}")

print("\nStudent dict: ")
print(f"Name: {Student.get("name")}")
print(f"Age: {Student.get("age")}")
print(f"Grade: {Student.get("grade")}")
