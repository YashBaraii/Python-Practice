# Check if input age is between 18 and 60.

is_between = lambda age: 18 <= age <= 60

age = int(input("Enter your age: "))

if is_between(age):
    print("Yes, your age is between 18 and 60. Means you are an adult.")
else:
    print("No, your age is not between 18 and 60. Means you are not an adult.")
