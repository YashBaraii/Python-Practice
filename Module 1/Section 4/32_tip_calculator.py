# Build a simple tip calculator.


def split_bill_amount(total_bill_amount, n_of_person):
    split_amount = total_bill_amount / n_of_person
    return float(f"{split_amount:.2f}")


def tip_calc(tip_percentage, bill_amount):
    tip_amount = bill_amount * (tip_percentage / 100)
    total_bill_amount = bill_amount + tip_amount

    return tip_amount, total_bill_amount


bill_amt = float(input("Enter your bill amount (₹): "))
tip_percentage = float(input("Enter your tip percentage (%): "))

tip_amt, total_bill_amt = tip_calc(tip_percentage, bill_amt)
print(f"\nThe Tip amount on bill amount ₹ {bill_amt} is: ₹ {tip_amt}")
print(f"Means, the Total bill amount is: {total_bill_amt}")

n_of_person = int(input("\nEnter the number of person: "))
split_amt = split_bill_amount(total_bill_amt, n_of_person)
print(f"\nThe split to be paid by each is: ₹ {split_amt}")
