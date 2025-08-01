#   Use map() to convert a list of temperatures from C to F.

convert = lambda c: round((c * (9 / 5)) + 32, 3)

lst_c = [34, 1, 65, 77, 42, 29]
print("\nThe list of temperatures in celsius: ", lst_c)

lst_f = list(map(convert, lst_c))

print("\nThe list of temperature in fahrenheit: ", lst_f)
