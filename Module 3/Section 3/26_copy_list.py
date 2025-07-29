# Copy a list without using copy() method.

lst = [num for num in range(1, 6)]

print("\nMain list: ", lst)


new_lst = lst
print("\nNew list (Both main and this list changes seamlessly):  ", new_lst)


copy_lst = [item for item in lst]

print("Copy list (Doesn't make any changes to main list): ", copy_lst)
