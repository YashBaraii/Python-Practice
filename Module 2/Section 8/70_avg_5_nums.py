# Ask for 5 numbers and print the average.


lst = list(map(int, input("Enter 5 numbers separated by comma: ").split(",")))

print(f"The Average of these 5 numbers is: {sum(lst) / len(lst) :.2f}")

print(
    "Average: ",
    sum(nums := list(map(int, input("Enter 5 numbers: ").split(" ")))) / len(nums),
)
