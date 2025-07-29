# Check if an element exists in a tuple.

check = lambda tup, e: e in tup

tup = (1, 2, 3, 4, 5)

print(f"\nTuple: ", tup)
num = int(input("\nEnter element for checking its existence: "))

if check(tup, num):
    print(f"Yes, {num} exists in the tuple.")
else:
    print(f"Not, {num} doesn't exists in the tuple.")
