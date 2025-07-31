# Function to return the sum of elements in a list.


def ele_sum(lst):
    return sum(lst)


lst = [1, 2, 3, 4, 5]

print(f"\nList: ", *lst)
print(f"The sum of all elements in above list is: {ele_sum(lst)}")
