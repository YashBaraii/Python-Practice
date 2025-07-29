# Rotate a list to the right by 2 positions.

rotate_right_by_2 = lambda lst: lst[-2:] + lst[:-2]

lst = [1, 2, 3, 4, 5]
print(f"\nOriginal list: {lst}")

lst = rotate_right_by_2(lst)
print("List rotated to right by 2 positions: ", lst)
