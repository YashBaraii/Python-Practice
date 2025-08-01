#   Use filter() to keep names starting with "A".

does_starts_with_A = lambda name: name.strip().lower().startswith("a")
# does_starts_with_A = lambda name: name.strip().lower()[0] == "a"

names = ["Raj", " Aman", "Suraj", "Dhiraj", "Arun", "aditya"]

print(f"\nList of names: ", names)

a_initials_names = list(filter(does_starts_with_A, names))
print(f"Here are the names that starts with A: \n", a_initials_names)
