# Print a countdown from 10 to 0.


def countdown():
    i = 10
    while True:
        if i < 0:
            break
        print(f"{i}")
        i -= 1


print("\nCountdown till 0")
countdown()
