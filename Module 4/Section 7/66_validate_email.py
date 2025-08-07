#   Function to validate an email address (basic check).

# yashbarai@gmail.com


def is_valid(email):
    if "." not in email or "@" not in email:
        return False

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username or not domain:
        return False

    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    return True


emails = [
    "john.doe@example.com",
    "noatsymbol.com",
    "missingdomain@",
    "@nouser.com",
    "incomplete@domain",
    "valid.email@domain.co",
]


for i, email in enumerate(emails):
    print(f"{i+1}. {email}: IsValid - {is_valid(email)}")
