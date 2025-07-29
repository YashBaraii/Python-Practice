# # Find all prime numbers in a range given by the user.


# def is_palindrome(n):
#     return int(str(abs(n))[::-1]) == abs(n)


# def find_nums():
#     nums = []

#     for num in range(100, 1000):
#         if is_palindrome(num):
#             nums.append(num)

#     return nums


# find_nums2 = lambda: [
#     num for num in range(100, 1000) if int(str(abs(num))[::-1]) == num
# ]

# nums = find_nums2()

# print(f"All the prime numbers between 100 and 999 are as follows: \n{nums}")
print(f"All the prime numbers between 100 and 999 are as follows: ")

print(
    " ".join(
        str(num) for num in range(100, 1000) if int(str(abs(num))[::-1]) == abs(num)
    )
)
