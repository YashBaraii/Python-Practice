# Function to merge two dictionaries.


def merge1(d1, d2):
    return d1 | d2


def merge2(d1, d2):
    return {**d1, **d2}


d1 = {1: 1, 2: 2, 3: 3}
d2 = {3: 3, 4: 4, 5: 5}

print(merge1(d1, d2))
