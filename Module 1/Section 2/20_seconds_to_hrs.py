# Convert seconds into hours, minutes, seconds.


input_seconds = int(input("Enter the seconds: "))

seconds = input_seconds

minutes = int(seconds / 60)

hours = int(minutes / 60)

minutes = minutes - (hours * 60)

seconds = seconds - (hours * 3600) - (minutes * 60)

print(
    f"\n{input_seconds} seconds are {hours} hrs, {minutes} min and {seconds} seconds."
)
