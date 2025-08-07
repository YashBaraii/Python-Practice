#  Write a decorator-like function that logs the result of another function


def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Function '{func.__name__} returned: {result}")
        return result

    return wrapper


@log_result
def add(a, b):
    return a + b


@log_result
def greet(name):
    return f"Hello, {name}"


add(6, 8)
greet("Yashya")
