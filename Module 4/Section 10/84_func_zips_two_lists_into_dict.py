# Function that zips two lists into a dictionary


def zip_lists(lst1, lst2):
    return dict(zip(lst1, lst2))


nums = [num for num in range(1, 11)]
squares = [num * num for num in range(1, 11)]

dict = zip_lists(nums, squares)

print("\nThe squares of numbers from 1-10: ")
for num, square in dict.items():
    print(f"{num} - {square}")
