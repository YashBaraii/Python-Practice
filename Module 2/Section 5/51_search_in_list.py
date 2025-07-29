# Search for an element in a list using a loop.


def is_found(lst, x):
    for i in lst:
        if i == x:
            return True

    return False


# lst = [1, 3, 4, "Yash", 180.8]
lst = [1, 3, 4, 5, 6]
print("\nList: ", lst)

search = int(input("What do you want to search: "))

if is_found(lst, search):
    print(f"{search} found in the list")
else:
    print(f"{search} not found in the list")
