# Sort a dictionary by values.

import random

sort_dict = lambda dictt: dict(sorted(dictt.items(), key=lambda item: item[1]))

lst1 = [num for num in range(1, 6)]
lst2 = [num * num for num in range(1, 6)]

dictt = dict(zip(lst1, lst2))
items = list(dictt.items())
random.shuffle(items)
dictt = dict(items)
print("\nOriginal unsorted dict: ", dictt)

sorted_dictt = sort_dict(dictt)
print(f"Sorted dict: {sorted_dictt}")
