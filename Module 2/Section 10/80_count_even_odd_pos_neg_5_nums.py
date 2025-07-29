# Take 5 numbers and print how many are even, odd, positive, negative.

get_even_count = lambda a, b, c, d, e: len(
    [num for num in [a, b, c, d, e] if num % 2 == 0]
)

get_positive_count = lambda a, b, c, d, e: len(
    [num for num in [a, b, c, d, e] if num > 0]
)

a, b, c, d, e = map(int, input("\nEnter 5 numbers separated by comma: ").split(","))

odd_count = 5 - get_even_count(a, b, c, d, e)
negative_count = 5 - get_positive_count(a, b, c, d, e)

print("\nResults: ")
print(f"Even numbers count: {5 - odd_count}")
print(f"Odd numbers count: {odd_count}")
print(f"Postive numbers count: {5 - negative_count}")
print(f"Negative numbers count: {negative_count}")
