# Split a list into 2 halves.


def split_list(lst):
    lst1 = []
    lst2 = []
    for i in range(len(lst)):
        if i < int((len(lst) / 2)):
            lst1.append(lst[i])
        else:
            lst2.append(lst[i])
    return lst1, lst2


split_list2 = lambda lst: (lst[: (len(lst)) // 2], lst[(len(lst)) // 2 :])


lst = [1, 2, 3, 4, 5, 6, 7]

print("\nMain List: ", lst)


lst1, lst2 = split_list2(lst)
print("\nFirst list: ", lst1)
print("Second list: ", lst2)
