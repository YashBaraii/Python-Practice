# Reverse the list using .reverse() and slicing.


def reverse1(lst):
    temp = lst.copy()
    temp.reverse()
    return temp


reverse2 = lambda lst: lst[::-1]


lst = [1, 2, 3, 4, 5]


print("\nOriginal list: ", lst)

print("\nReversed by .reverse(): ", reverse1(lst))
print("\nReversed by slicing: ", reverse2(lst))
