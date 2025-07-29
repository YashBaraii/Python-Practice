# Remove all special characters from a string.

import re

st = "Hey there, myself Yash Barai. I live in Los Angelas."
print("Original String: ", st)

filtered = re.sub(r"[^a-zA-Z0-9]", " ", st)

print("\nFiltered string: ", filtered)
