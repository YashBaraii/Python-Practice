# Combine multiple dictionaries into one (handling duplicate keys).

lst_of_dicts = [
    {"Avatar": 9.9, "Dabang": 10, "Dhishoom": 9},
    {"apple": 10, "banana": 12, "cat": 2},
]

dict = {}
for d in lst_of_dicts:
    for k, v in d.items():
        if k in dict:
            print(f"⚠️ Duplicate key '{k}' found. Overwriting existing value.")
        dict[k] = v
print("\nDisplaying Dictionaries from a dictionary: \n")
for k, v in dict.items():
    print(f"{k}: {v}")
