# Number guessing game with limited attempts.

import random

count = 0
max_attempts = 10
max_target = 100
target = random.randint(1, max_target)

print("\n--- Guess The Number Game ---\n")
print(
    f"You have to guess the number between 1 and {max_target} in {max_attempts} attempts only."
)

while True:
    guess = int(input("\nEnter your guess: "))
    count += 1

    if guess < target:
        print("--- Try Higher !")
    elif guess > target:
        print("--- Try Lower !")
    elif count > max_attempts:
        print(
            f"\nYou loose ! You couldn't guess the number in {max_attempts} attempts."
        )
    else:
        print(f"\nCongrats you win, you have guessed the number in {count} attempts. ")
        break
