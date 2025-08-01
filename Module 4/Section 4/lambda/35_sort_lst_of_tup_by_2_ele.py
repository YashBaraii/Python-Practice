# Sort a list of tuples by second element using lambda

lst_of_tups = [(8, 3, 2), (2, 1, 3), (7, 2, 4)]

print("\nOriginal List of tuples: ")
for tup in lst_of_tups:
    print(*tup)

print()

print("Sorted version: ")
sorted_lst_of_tups = sorted(lst_of_tups, key=lambda tup: tup[1])
for tup in sorted_lst_of_tups:
    print(*tup)
