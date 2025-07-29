# Create a dictionary where key = number and value = square of the number.

lst_num = [num for num in range(1, 11)]
lst_squares = [num * num for num in lst_num]

dictt = dict(zip(lst_num, lst_squares))

print("\nThe dictionary of squares of numbers (1-10):")
print(dictt)
