# Take input for a password and print "Strong" if it’s >8 characters and has both letters and digits.


def check(pw):
    if len(pw) < 8:
        print("Your password is weak.")
        return

    has_letter = False
    has_digit = False

    for ch in pw:
        if ch.isalpha():
            has_letter = True
        elif ch.isdigit():
            has_digit = True

    if has_digit and has_letter:
        print("Your password is strong.")
    else:
        print("Your password is week.")


password = input("\nEnter your password: ")
check(password)
