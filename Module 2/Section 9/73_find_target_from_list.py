# Randomly select a number from a list until the target number is found.

import random

lst = [1, 3, 5, 2, 4, 6, 8]
count = 0

print(f"\nList of numbers: {lst}")
target = int(input("Enter your target: "))

while True:

    guess = random.choice(lst)

    print(f"\nBot's guess is {guess}")
    count += 1

    if target == guess:
        print(f"\n---Bot guess your target in {count} attempts.")
        break
