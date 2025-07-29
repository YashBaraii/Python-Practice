# Print multiplication table of a number.

num = int(input("Enter the number: "))

print(*(f"{num} x {i} = {num*i}" for i in range(1, 11)), sep="\n")
