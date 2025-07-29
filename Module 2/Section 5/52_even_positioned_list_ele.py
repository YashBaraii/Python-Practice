# Print only even-positioned elements in a list.


def print_ele(lst):
    print(" ".join(str(lst[i]) for i in range(len(lst)) if i % 2 == 0))


print_ele2 = lambda lst: print(*(str(lst[i]) for i in range(0, len(lst), 2)))

lst = [1, 2, 4, 5, 6]
print_ele2(lst)
