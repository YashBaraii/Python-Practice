# Function to convert Celsius to Fahrenheit.


def cel_to_fah(celsius):
    return (celsius * (9 / 5)) + 32


celsius = float(input("\nEnter the temperature in celsius (C): "))
print(f"Its conversion into fahrenheit is: {cel_to_fah(celsius)} F")
