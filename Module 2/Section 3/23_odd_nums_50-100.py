# Print all odd numbers from 50 to 100.

print("\nAll odd numbers between 50 and 100:")

print(*(num for num in range(50, 101) if num & 1 == 1), sep=" ")
