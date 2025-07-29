# Simple password strength checker using conditions and loops.


def check_strength(pw):
    score = 0
    if len(pw) >= 8:
        score += 1

    have_uppercase = have_lowercase = have_number = have_special_char = False

    for ch in pw:
        if ch.islower():
            have_lowercase = True
        elif ch.isupper():
            have_uppercase = True
        elif ch.isdigit():
            have_number = True
        elif not ch.isalnum():
            have_special_char = True

        if have_uppercase and have_lowercase and have_number and have_special_char:
            break

    score += have_lowercase + have_uppercase + have_number + have_special_char

    if score <= 2:
        result = "Weak Password"
    elif score == 3:
        result = "Moderate Password"
    else:
        result = "Strong Password"

    return result, score


password = input("\nEnter your password: ")

result, score = check_strength(password)

print(f"{password} is a {result}. And score is: {score}")
