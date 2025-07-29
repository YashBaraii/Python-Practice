# Print all even numbers from 1 to 100.

print("All Even numbers between 1 and 100")
print(" ".join(str(num) for num in range(1, 101) if num & 1 == 0))
