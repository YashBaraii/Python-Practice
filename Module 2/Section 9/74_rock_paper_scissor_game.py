# Rock-paper-scissors game (text-based).

import random

options = ["rock", "paper", "scissor"]

bots_score = 0
users_score = 0

MAX_SET = 3
count_set = 0

choice_to_play = lambda num: "rock" if num == 1 else "paper" if num == 2 else "scissor"

is_user_winner = lambda b_s, u_s: True if u_s > b_s else -1 if u_s == b_s else False

while True:

    if count_set == MAX_SET:
        result = is_user_winner(bots_score, users_score)
        print("\n\nFinal Results: ")
        if result is True:
            print("\n--- You win ! ---\n")
        elif result == -1:
            print("\n--- Its a tie! ---\n")
        else:
            print("\n--- You loose ! ---\n")

        print(f"Bot's Score: {bots_score} | Your Score: {users_score}")
        break

    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissor")

    try:
        users_choice = int(input("What's your play (x): "))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue

    if not 0 < users_choice < 4:
        print("\nInvalid Choice !")
        continue

    users_play = choice_to_play(users_choice)

    bots_play = random.choice(options)

    print(f"\nBot's Play: {bots_play}")
    print(f"Your Play: {users_play}\n")

    if (
        (bots_play == "rock" and users_play == "rock")
        or (bots_play == "paper" and users_play == "paper")
        or (bots_play == "scissor" and users_play == "scissor")
    ):
        print("--- Its a tie !")
        count_set += 1
        continue

    elif (
        (bots_play == "scissor" and users_play == "paper")
        or (bots_play == "paper" and users_play == "rock")
        or (bots_play == "rock" and users_play == "scissor")
    ):
        print("--- Bot win !")
        bots_score += 1

    else:
        print("--- You win !")
        users_score += 1

    count_set += 1
