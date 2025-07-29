# Determine if at least one out of 3 numbers is negative.

a, b, c = map(int, input("Enter 3 numbers separated by comma: ").split(","))

if a < 0 or b < 0 or c < 0:
    print("Yes, atleast one of these 3 numbers is negative.")
else:
    print("No, none one of these 3 numbers is negative.")
