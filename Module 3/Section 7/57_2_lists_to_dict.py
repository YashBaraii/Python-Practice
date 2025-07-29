# Create a dictionary from two lists (keys and values).


def convert(lst1, lst2):
    if len(lst1) != len(lst2):
        return None
    dictt = {}
    for i in range(len(lst1)):
        dictt[lst1[i]] = lst2[i]
    return dictt


convert2 = lambda lst1, lst2: None if len(lst1) != len(lst2) else dict(zip(lst1, lst2))


lst1 = [num for num in range(1, 6)]
lst2 = [num * num for num in range(1, 6)]

print(f"\nList 1: {lst1} | List 2: {lst2}")

merged_dict = convert2(lst1, lst2)

if merged_dict is None:
    print("Err: Dictionary can't be created, lengths of both lists is different.")

else:
    print("\nThe dictionary created by list 1 and list 2 is: ")
    for key, value in merged_dict.items():
        print(f"Square of {key} is: {value}")
