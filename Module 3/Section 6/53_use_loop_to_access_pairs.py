# Loop through a dictionary and print key-value pairs.

Student = {"name": "Yash", "age": 17, "email": "yash@gmail.com"}

for key in Student:
    print(f"\nKey: {key} and its value: {Student[key]}")

for key, value in Student.items():
    print(f"\nKey: {key} and its value: {value}")
