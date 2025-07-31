# Function that counts vowels in a string.

import time

current_time_struct = time.localtime()

am_pm = time.strftime("%p", current_time_struct)


def greet(name="User"):
    if am_pm == "AM":
        print(f"\nGood Morning, {name}")
    else:
        print(f"\nGood Afternoon, {name}")


greet("Yash")
