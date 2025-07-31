# Function using **kwargs to print key-value pairs.


def pairs(**kwargs):
    i = 1
    for k, v in kwargs.items():
        print(f"{i}. {k}: {v}")
        i += 1


pairs(name="Yash", age=17, gender="Male")
