# Create a dictionary to store a student's name, age, and grade.

name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
grade = input("Enter your grade: ")

Student = {"name": name, "age": age, "grade": grade}

print("\nStudent: ", Student)
