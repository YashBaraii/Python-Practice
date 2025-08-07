# Function that returns keys of a dictionary with value > 100.


def find_keys(dict):
    return [key for key, value in dict.items() if value > 100]


dict = {"K1": 10, "K2": 50, "K3": 101, "K4": 150}

print("\nDictionary: ", dict)

keys = find_keys(dict)

print("Here are the keys whose values are greated than 100: ", *keys)
