# Count how many numbers between 1–N are divisible by 7.


# def count_7_divisibles(n):
#     count = 0
#     for num in range(1, n + 1):
#         if num % 7 == 0:
#             count += 1
#     return count

count_7_divisibles2 = lambda n: n // 7

# num = int(input("Enter the number: "))

# print(f"The total 7 divisibles between 1 and {num} is: {count_7_divisibles(num)}")

print((int(input("Enter N: ")) // 7))
