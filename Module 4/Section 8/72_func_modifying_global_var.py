# Function that modifies a global variable

is_adult = False


def check_is_adult(age):
    global is_adult

    is_adult = True if age > 18 else False


age = int(input("\nEnter your age: "))
check_is_adult(age)

if is_adult:
    print("\nYou are an adult means you are now above 18.")
else:
    print("\nYou are not an adult means you are under 18.")
