# Find the key with the maximum value.

import random

find_max = lambda dictt: sorted(dictt.items(), key=lambda item: item[1], reverse=True)[
    0
][0]

find_max2 = lambda dictt: max(dictt, key=dictt.get)

lst1 = [num for num in range(1, 6)]
lst2 = [num * num for num in range(1, 6)]

dictt = dict(zip(lst1, lst2))
items = list(dictt.items())
random.shuffle(items)
dictt = dict(items)

print("\nDictionary: ", dictt)


print("The key that have maximum value is: ", find_max2(dictt))
