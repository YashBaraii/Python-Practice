# Evaluate an expression: a + b * c / d – e, input from user.

evaluate = lambda a, b, c, d, e: a + ((b * c) / d) - e

try:

    a, b, c, d, e = map(int, input("Enter 5 numbers separated by comma: ").split(","))

    if d == 0:
        print("Err: Division by Zero is not allowed !")
    else:
        result = evaluate(a, b, c, d, e)
        print(f"Result: {result:.2f}")
except ValueError:
    print("Invalid Input: Please enter exactly 5 numbers.")
