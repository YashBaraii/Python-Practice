# Create a program that accepts comma-separated numbers and stores them in a tuple and a list.

lst = list(map(int, input("Enter 3 number separated by comma: ").split(",")))
tup = tuple(map(int, input("Enter 3 number separated by comma: ").split(",")))

print("List: ", lst)
print("Tuple: ", tup)
