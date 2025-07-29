# Simulate rolling a die 10 times.
import random


# def roll_a_die():
#     return random.randint(1, 6)


# for _ in range(10):
#     result = roll_a_die()
#     print(f"Rolling a die: {result}")


print("\n".join(f"Rolling a die: {random.randint(1, 6)}" for _ in range(10)))
