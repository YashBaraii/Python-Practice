#   Use filter() to get even numbers from a list.

is_even = lambda n: n & 1 == 0

filter_evens = lambda lst: list(filter(is_even, lst))

lst = [1, 2, 3, 4, 5]

print(f"\nList: ", *lst)

print(filter_evens(lst))
