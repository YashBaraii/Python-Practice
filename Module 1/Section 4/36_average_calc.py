# Take input of two numbers and show the average.

calc_avg = lambda n1, n2: round(((n1 + n2) / 2), 2)

a, b = map(float, input("\nEnter two numbers separated by comma: ").split(","))
avg = calc_avg(a, b)
print(f"\nThe average of two numbers is: {avg}")
