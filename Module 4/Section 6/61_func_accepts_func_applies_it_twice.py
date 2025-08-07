# Write a function that accepts another function and applies it twice.


def main_func(func, arg):
    return func(func(arg))


func = lambda n: n * n

print(main_func(func, 2))
