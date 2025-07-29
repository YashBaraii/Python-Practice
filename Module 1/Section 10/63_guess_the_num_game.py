# A number guess game: Ask user to guess a number between 1-10. If correct, print "You win!"

import random

MAX_TARGET_LIMIT = 1000

target = random.randint(1, MAX_TARGET_LIMIT)


print("\nWelcome to the GUESS THE NUMBER game !")
print(f"You have to guess the number between 1 and {MAX_TARGET_LIMIT}")

MAX_GUESS_LIMIT = 15
no_of_guesses = 0

while True:
    guess = int(input("\nEnter your guess: "))

    if guess < target:
        print("Try Higher !")
    elif guess > target:
        print("Try Lower !")
    elif guess == target:
        print(
            f"\n\nYou wind !, you have guessed the number '{target}'. You have guessed the number in {no_of_guesses} attempts."
        )
        break
    elif no_of_guesses == MAX_GUESS_LIMIT:
        print("\nYou loose ! You took more than 10 guesses !")

    no_of_guesses += 1
