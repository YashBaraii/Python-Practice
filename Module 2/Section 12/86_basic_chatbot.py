# Check user input and respond with basic chatbot logic (simple rules).

import time
import re


def is_greeting(user_input):
    return "hello" in user_input or "hi" in user_input


def is_asking_time(user_input):
    return "what" in user_input and "time" in user_input


def is_asking_addition(user_input):
    return ("add" in user_input or "sum" in user_input) and ("numbers" in user_input)


def is_ending_chat(user_input):
    return (
        "bye" in user_input
        or "exit" in user_input
        or "end" in user_input
        or "stop" in user_input
    )


def respond(user_input):
    user_input = user_input.lower()
    if is_greeting(user_input):
        return f"Hello, I am your personal chatbot. You can ask me about anything, anytime, anywhere !"

    if is_asking_time(user_input):
        return f"The current time is: {time.strftime('%I:%M %p')}"

    if is_asking_addition(user_input):
        # nums = []
        # for n in user_input:
        #     if n.isdigit():
        #         nums.append(n)

        nums = list(map(int, re.findall(r"\d+", user_input)))
        if len(nums) < 2:
            return "Please provide at least two numbers to add."

        a, b = nums[0], nums[1]
        result = int(a) + int(b)
        return f"The Result of {a} + {b} is: {result}"

    if is_ending_chat(user_input):
        return f"Bye sir, have a great day !"

    return "Sorry, I didn't understand that."


while True:
    user_input = input("\nAsk anything: ")
    user_input_response = respond(user_input)

    print(f"\nYou: {user_input}")
    print(f"Chatbot: {user_input_response}")

    if "Bye" in user_input_response:
        break
