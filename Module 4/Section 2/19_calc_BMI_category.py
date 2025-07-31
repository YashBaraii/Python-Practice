# Create a function to calculate BMI and return category.


def bmi_category(weight, height):
    bmi = weight / (height * height)
    category = "Can't say anything"
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 22.9:
        category = "Normal"
    elif 23 <= bmi <= 24.9:
        category = "Overweight"
    elif 25 <= bmi <= 29.9:
        category = "Obese I"
    else:
        category = "Obese II"

    return bmi, category


weight, height = map(float, input("\nEnter your weight (kg) and heigt(m): ").split())

bmi, category = bmi_category(weight, height)

print(f"Your Body Mass Index (BMI) is: {bmi:.2f} kg/m.sq")
print(f"Your BMI Category is: {category}")
