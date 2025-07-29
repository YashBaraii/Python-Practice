# Check if a year is a leap year.


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False


year = int(input("Enter the year (YYYY): "))

if is_leap_year(year):
    print(f"\n{year} is a leap year.")
else:
    print(f"\n{year} is not a leap year.")
