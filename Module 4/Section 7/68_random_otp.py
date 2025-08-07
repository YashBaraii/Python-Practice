# Function to generate random OTP.

import random


def generate_otp():
    return random.randint(1000, 9999)


print(f"\nYour OTP is: {generate_otp()}")
