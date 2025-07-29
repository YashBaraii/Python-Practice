# Calculate BMI: weight / (height in m)^2.

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

BMI = weight / (height * height)

print(f"\nYour Body Mass Index (BMI) is: {BMI:.2f}")
