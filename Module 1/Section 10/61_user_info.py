# Take input of name, age, height. Print a formatted message:
# "Hi, my name is John, I am 25 years old, and 5.9 feet tall."


def show_msg(name, age, height):
    print(f"\nHi, my name is {name}, I am {age} years old, and {height} feet tall.")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

show_msg(name, age, height)
