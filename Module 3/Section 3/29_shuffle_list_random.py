# Shuffle a list (use random.shuffle()).

import random

lst = [num for num in range(1, 6)]
print(f"\nOriginal list: {lst}")

random.shuffle(lst)

print("Its shuffled and randomized version: ", lst)
