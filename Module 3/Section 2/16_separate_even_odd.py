# Separate even and odd numbers from a list.

lst = [1, 2, 3, 4, 5]

even = []
odd = []
for item in lst:
    if item % 2 == 0:
        even.append(item)
    else:
        odd.append(item)

print("\nList: ", lst)

print("All the even numbers: ", even)
print("All the odd numbers: ", odd)
