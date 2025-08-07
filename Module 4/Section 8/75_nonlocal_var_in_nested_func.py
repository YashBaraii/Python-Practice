# Use nonlocal to track state in nested functions


def counter():
    count = 0

    def increment():
        nonlocal count

        count += 1
        return count

    return increment


c = counter()

print(c())
print(c())
print(c())
print(c())
print(c())
