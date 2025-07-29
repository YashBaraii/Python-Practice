# Check membership of an element in a set.

st = {num for num in range(1, 11)}

num = int(input("\nEnter the number: "))

if num in st:
    print(f"Yes, {num} is present in the set.")
else:
    print(f"No, {num} is not present in the set.")
