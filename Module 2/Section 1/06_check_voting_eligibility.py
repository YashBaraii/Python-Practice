# Check if a person is eligible to vote (18+).

is_eligible = lambda age: True if age >= 18 else False

age = int(input("Enter your age: "))

if is_eligible(age):
    print("Congrats, you are eligible to vote")
else:
    print(f"Oh no, you aren't eligible to vote, you have wait {18 - age} years.")
