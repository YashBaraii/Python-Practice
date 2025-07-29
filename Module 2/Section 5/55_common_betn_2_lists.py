# Print common elements from two lists.


def common_ele(lst1, lst2):
    common = []
    for ele1 in lst1:
        if ele1 in lst2:
            common.append(ele1)
    return common


lst1 = [1, 4, 6, 7, 9]
lst2 = [1, 5, 10, 7, 19]


print("The common elements in both the lists are as follows: ")
common = common_ele(lst1, lst2)

common2 = list(set(lst1) & set(lst2))
print(common2)
