# Function that finds all even numbers in a list.


def find_evens(lst):
    return [num for num in lst if num & 1 == 0]


lst = [num for num in range(1, 7)]
print(f"\nList: {lst}")

evens = find_evens(lst)
print(f"All the even numbers in above list are: ", *evens)
