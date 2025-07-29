# Continue taking input until the user enters "exit".


def sum(a, b):
    print(f"\nThe Result of {a} + {b} is: {a + b}")


def diff(a, b):
    print(f"\nThe Result of {a} - {b} is: {a - b}")


while True:
    print("\n1. Add two numbers")
    print("2. Subtract two numbers")
    print("-> Type 'exit' to close the script.")

    choice = input("\nEnter your choice (1, 2, exit): ")

    match (choice):
        case "1":
            num1, num2 = map(
                int, input("\nEnter two numbers separated by comma: ").split(",")
            )
            sum(num1, num2)
        case "2":
            num1, num2 = map(
                int, input("\nEnter two numbers separated by comma: ").split(",")
            )
            diff(num1, num2)
        case "exit":
            print("\nExiting the script !")
            break
        case _:
            print("\nPlease enter valid option !")
