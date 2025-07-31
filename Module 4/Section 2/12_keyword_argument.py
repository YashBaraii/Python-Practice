# Function with keyword arguments.


def greet(name, message="Hello"):
    print(f"{name}: {message}")


greet("Charlie")
greet("Bob", "How are you ?")
print()

greet(name="Raja")
greet(name="Sham", message="Jevan zal kai ?")
print()

greet("Rohan", message="Hi varun")
