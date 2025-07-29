# Check if a list is sorted.


def check(lst):
    asc = sorted(lst)
    des = sorted(lst, reverse=True)
    return lst == asc or lst == des


lst1 = [num for num in range(1, 5)]
lst2 = [num for num in range(5, 0, -1)]
lst3 = [2, 5, 1, 4, 3]


for i, lst in enumerate([lst1, lst2, lst3]):
    print(f"\nList {i+1}: {lst}")
    if check(lst):
        print(f"List {i+1} is sorted.")
    else:
        print(f"List {i+1} is not sorted.")
