# Given a list of email addresses, count how many come from each domain


def count_domains(emails):
    domain_counts = {}
    for email in emails:
        domain = email[(email.index("@")) + 1 :]
        if domain in domain_counts:
            domain_counts[domain] += 1
        else:
            domain_counts[domain] = 1
    return domain_counts


email_addresses = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "charlie@hotmail.com",
    "dave@gmail.com",
    "eve@yahoo.com",
    "frank@outlook.com",
    "grace@gmail.com",
    "heidi@protonmail.com",
    "ivan@yahoo.com",
    "judy@gmail.com",
    "mallory@outlook.com",
    "nia@icloud.com",
    "oscar@gmail.com",
    "peggy@protonmail.com",
    "trent@outlook.com",
    "victor@icloud.com",
    "walter@gmail.com",
    "zoe@yahoo.com",
]

counts = count_domains(email_addresses)

print("\nHere are the stats of domains: \n")
for domain, count in counts.items():
    print(f"{domain} x {count} emails.")
