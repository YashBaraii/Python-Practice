# Calculate the simple interest given principal, rate, and time.


si_calc = lambda p, r, t: p * (r / 100) * t
total_amt = lambda si, p: si + p

principal_amt = float(input("\nEnter the principal amount (₹): "))
rate = float(input("Enter the rate of interest (%): "))
time = int(input("Enter the time (years): "))

si_amt = si_calc(principal_amt, rate, time)
print(f"\nThe Calculated Simple Interest is: {si_amt}")
print(f"The Total amount is: {total_amt(si_amt, principal_amt)}")
