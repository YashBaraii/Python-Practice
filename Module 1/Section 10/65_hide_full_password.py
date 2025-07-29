# Take input of a 4-digit number and mask all digits except the last (like password fields).

masked_password = lambda pw: "*" * (len(pw) - 1) + pw[-1]

password = input("\nEnter your 4-digit password: ")

if len(password) != 4 and password.isdigit():
    print("Password must be a 4-digit number")
else:
    print(f"Your masked password is: {masked_password(password)}")
