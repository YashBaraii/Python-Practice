# Determine if a year is a leap year.


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Enter the year: "))

if is_leap_year(year):
    print(f"\n{year} is a Leap year")
else:
    print(f"\n{year} is not a Leap year")
