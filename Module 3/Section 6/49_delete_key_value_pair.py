# Delete a key-value pair using pop().

Student = {"name": "Yash", "age": 17, "grade": "A"}
Student["email"] = "yash@gmail.com"


print("\nStudent dict: ")
print(f"Name: {Student.get("name")}")
print(f"Age: {Student.get("age")}")
print(f"Grade: {Student.get("grade")}")
print(f"Email: {Student.get("email")}")

Student.pop("grade")

print(Student)
print(f"Grade: {Student.get("grade")}")
