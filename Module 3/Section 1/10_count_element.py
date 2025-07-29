# Count how many times an element appears in the list.

lst = [1, 2, 3, 3, 4, 5, 3, 2, 1, 1, 3]

print("\nList: ", lst)

num = int(input("Enter which value's count you want: "))

print(f"The count of {num} is: {lst.count(num)}")
