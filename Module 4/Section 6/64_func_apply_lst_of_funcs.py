# Write a function that applies a list of functions to a single input.


def main_func(x, y):
    add = lambda a, b: a + b
    diff = lambda a, b: a - b
    prod = lambda a, b: a * b
    div = lambda a, b: a / b if b != 0 else f"Err: Can't divide by zero"

    lst = [("add", add), ("diff", diff), ("prod", prod), ("div", div)]
    results = {}
    for name, func in lst:
        results[name] = func(x, y)

    return results


results = main_func(2, 7)

for index, (func, result) in enumerate(results.items(), 1):
    print(f"{index}. {func}: {result}")
