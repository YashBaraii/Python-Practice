# Function that accepts both *args and **kwargs.


def func(*args, **kwargs):
    print(sum(args))
    for k, v in kwargs.items():
        print(f"{k} - {v}")


func(1, 2, 3, 4, 5, name="Yash", age=17, gender="Male")
