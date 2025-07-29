# Take input age and print if the person is eligible to vote (18+).

age = int(input("Enter your age *REAL ONE*: "))

if age < 18:
    print(
        f"\nUnfortunately, you aren't eligible to vote, you still need to wait {18 - age} years."
    )
else:
    print("\nCongratulations, you are eligible to vote")
