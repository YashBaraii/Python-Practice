# Merge two dictionaries.


def merge_dict(d1, d2):
    lst_d1 = list(d1.items())
    lst_d2 = list(d2.items())
    lst_d1.extend(lst_d2)
    return dict(lst_d1)


d1 = {1: 1, 2: 4, 3: 9, 4: 166}
d2 = {4: 16, 5: 25, 6: 36}

print(f"\nDict 1: {d1} | Dict 2: {d2}")

merged_dict = merge_dict(d1, d2)
merged_dict2 = {**d1, **d2}

print(f"Their merged version: {merged_dict}")
print(f"Their merged version: {merged_dict2}")
