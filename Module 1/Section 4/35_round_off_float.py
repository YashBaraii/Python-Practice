# Take a float input and round it to 2 decimal places.


def round_off1(num):
    return float(f"{num:.2f}")


def round_off2(num):
    return round(num, 2)


round_off3 = lambda num: round(num, 2)


input = float(input("\nEnter float number: "))
print(f"Round off number of {input} is: {round_off1(input)} ")
