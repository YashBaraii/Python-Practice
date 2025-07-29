# Convert days to weeks and days.


def convert(days):
    wordings_list = [7, 1]
    for i in wordings_list:
        count = days // i
        print(f"{i} x {count}")
        days %= i


days = int(input("\nEnter the number of days: "))
convert(days)
