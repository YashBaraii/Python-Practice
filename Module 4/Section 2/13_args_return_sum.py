# Write a function that takes any number of arguments using *args and returns their sum.


def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5))
