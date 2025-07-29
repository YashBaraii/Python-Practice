# Input 3 numbers and print them in ascending order.


def print_in_order(a, b, c):
    lst = [a, b, c]
    for _ in range(3):
        print(min(lst), end=" ")
        lst.remove(min(lst))


print_in_order2 = lambda a, b, c: print(" ".join(map(str, sorted([a, b, c]))))

a, b, c = map(int, input("Enter 3 numbers separated by comma: ").split(","))

print_in_order2(a, b, c)
