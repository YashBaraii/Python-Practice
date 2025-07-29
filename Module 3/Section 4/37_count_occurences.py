# Count occurrences of an element in a tuple.

count = lambda tup, e: sum([1 for item in tup if item is e])

tup = (1, 3, 2, 2, 1, 4, 1, 5)
print(f"Tuple: {tup}")

num = int(input("\nEnter the element whose occurence count you want: "))

print(f"'{num}' occurs {count(tup, num)} times in the tuple.")
