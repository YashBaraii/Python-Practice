#  Function that checks for balanced parentheses


def is_balanced(exp):
    stack = []

    for ch in exp:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()

    return not stack


exp = input("\nEnter the mathematical expression with parentheses: ")

if is_balanced(exp):
    print("\nYes, this expression is perfectly balanced with parentheses.")
else:
    print("\nNo, this expression is not balanced with parentheses.")
