# Find all indices of a given element in a list.


def find_ele_indices(lst, ele):
    return [i for i in range(len(lst)) if lst[i] == ele]


lst = [1, 3, 2, 1, 4, 5, 1]

print(f"List: {lst}")
num = int(input("\nEnter the values whose indices you want find: "))

indices = find_ele_indices(lst, num)

print(f"These are all the indices of value {num} in the list: {indices}")
