# Write a function that returns a list of squares from 1 to n.


def lst_of_squares(n):
    return [num * num for num in range(1, n + 1)]


num = int(input("\nEnter the number: "))
list_squares = lst_of_squares(num)

print(f"Here is the list of squares from 1 - {num}: \n", *list_squares)
