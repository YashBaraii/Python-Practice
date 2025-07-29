# Print first N terms of a geometric progression.

# formula: Tn = a * r ^(n - 1)
# : a = first term
# : r = ratio
# : n = term number


def print_gp(a, r, n):
    print(f"\nThe first {n}th terms of a geometric progression are as follows: ")

    for i in range(n):
        term = a * (r**i)
        print(term, end=" ")


first_term = int(input("Enter the first term: "))
ratio = int(input("Enter the ratio: "))
n = int(input("Enter the number of terms: "))

print_gp(first_term, ratio, n)
