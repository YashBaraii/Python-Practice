# Print the top 3 most frequent elements in a list.

from collections import Counter


def find_top_3(lst):
    ele_counts = {}
    for item in lst:
        if item in ele_counts:
            ele_counts[item] += 1
        else:
            ele_counts[item] = 1

    return sorted(ele_counts, key=lambda k: ele_counts[k], reverse=True)[:3]


def find_top_3_2(lst):
    return [item for item, count in Counter(lst).most_common(3)]


lst = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]

print("\nList: ", lst)

top_3 = find_top_3_2(lst)
print(f"Top 3 most frequent elements are: ", *top_3)
