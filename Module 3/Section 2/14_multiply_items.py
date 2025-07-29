# Multiply all items in a list.

lst = [2, 2, 2, 2, 2]

print("List: ", lst)

product = 1

for item in lst:
    product *= item

print(f"The multiplication of all the items of this list is: {product}")
