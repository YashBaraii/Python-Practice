# Find the sum of all digits in all even numbers from 1 to N.


sum_of_even_digits = lambda n: sum(range(0, n + 1, 2))

num = int(input("\nEnter the number: "))

print(f"The sum of all the even numbers from 1 to {num} is: {sum_of_even_digits(num)}")
