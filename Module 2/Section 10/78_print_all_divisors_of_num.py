# # Take a number and print all its divisors.


# def print_divisors(n):
#     print(f"\nAll the divisors of {n} are as follows: ")
#     for num in range(1, n + 1):
#         if n % num == 0:
#             print(num, end=" ")


# num = int(input("Enter the number: "))
# print_divisors(num)


print(
    f"\nAll the divisors of {(num := int(input("Enter the number: ")))} are as follows: "
)
print(" ".join(str(n) for n in range(1, num + 1) if num % n == 0))
