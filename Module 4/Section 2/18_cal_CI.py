# Function to calculate the compound interest.


def calc_CI(P, r, n, t):
    return P * pow((1 + (r / n)), n * t)


principal = float(input("\nEnter your pricipal amount: ₹ "))
rate = float(input("Enter your rate of interest: "))
compouding_freq_n = int(input("Enter your compounding frequency: "))
time = float(input("Enter the time in years: "))

final_amount = calc_CI(principal, rate, compouding_freq_n, time)

print(f"\nThe Final amount is: ₹ {final_amount:.2f}")
