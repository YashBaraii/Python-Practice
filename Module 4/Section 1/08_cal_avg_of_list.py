# Function to calculate the average of a list.


def list_avg(lst):
    return sum(lst) / len(lst)


lst = [num for num in range(1, 6)]
print("\nList: ", *lst)

print("\nThe Average of list elements is: ", list_avg(lst))
