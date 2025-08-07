# Recursive function to sum all elements in a list


def sum_ele(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_ele(lst[1:])


lst = [num for num in range(1, 11)]
print(f"\nList: {lst}")

print(f"The sum of all the elements in the above list: {sum_ele(lst)}")
