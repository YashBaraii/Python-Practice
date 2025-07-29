# Build a basic flashcard quiz system using a dictionary (question: answer).

flashcards = {
    "What is the capital of France?": "Paris",
    "2 + 2 = ?": "4",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    "What is the largest planet in our Solar System?": "Jupiter",
    "What is the boiling point of water in Celsius?": "100",
}


try:
    print("\n----- FLASHCARD QUIZ SYSTEM -----\n")
    while True:
        ready_status = input("\nAre you ready to take quiz? (Y/n): ")
        if ready_status.lower() == "n" or len(ready_status) > 1:
            print("\nCome back soon! Whenever you are ready. ")
            break

        que_count = 1
        score = 0
        for que, ans in flashcards.items():
            answer = input(f"\n{que_count}. {que} ")
            que_count += 1

            if (
                answer == ans
                or answer.title() == ans
                or answer.upper() == ans
                or answer.lower() == ans
            ):
                print("-> ✅ Correct answer!")
                score += 1
            else:
                print("-> ❌ Wrong answer!")

        print(f"\nYour score is {score} out of 5\n")
        break

except KeyboardInterrupt:
    print("\n\nProgram interrupted by the user !")
