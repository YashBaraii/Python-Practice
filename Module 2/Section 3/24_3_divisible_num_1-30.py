# Print all numbers divisible by 3 between 1 to 30.

print("\nAll the numbers divisible by 3 between 1 to 30: ")
print(" ".join(str(num) for num in range(1, 31) if num % 3 == 0))
