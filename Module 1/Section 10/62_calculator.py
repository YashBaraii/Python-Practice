# A mini calculator that takes 2 numbers and an operator (+, -, *, /) from the user.

num1, num2 = map(int, input("\nEnter 2 numbers separated by comma: ").split(","))

operator = input("Enter your choice (+, -, *, /): ")
result = None

match (operator):
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("\nErr: Division by Zero is not allowed !")
    case _:
        print("\nInvalid choice !")

if result is not None:
    if result == int(result):
        print(f"\nThe Result of {num1} {operator} {num2} is: {int(result)}")
    else:
        print(f"\nThe Result of {num1} {operator} {num2} is: {result:.2f}")
