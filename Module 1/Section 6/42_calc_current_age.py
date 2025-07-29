# Ask the user their birth year and calculate current age.


def current_age1(year):
    return 2025 - year


current_age2 = lambda year: 2025 - year

birth_year = int(input("\nEnter your birth year (YYYY): "))
print(f"Your current age is: {current_age2(birth_year)}")
