# Function to group elements of a list by their length.


def group(lst):
    lst = [str(ele) for ele in lst]
    groups = {}
    for ele in lst:
        length = len(ele)
        if length not in groups:
            groups[length] = []
        groups[length].append(ele)

    return groups


lst = ["Hi", "My", "Name", "Yash", "I", "Love", "Ice cream", 123, 1, 3258, True, False]


print("\nList: ", *lst)

groups = group(lst)
groups = dict(sorted(groups.items()))

print()
for length, elements in groups.items():
    print(f"{length} - {elements}")
