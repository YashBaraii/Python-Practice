# Find the index of a character in a string.

st = "Hey, myself Yash, I live in Los Angelas"

print(f"String: {st}\n")

char = input("What character's index you want to find: ")

found = False

for i, ch in enumerate(st):
    if char == ch:
        print(f"'{char}' found in string at index: {i} and position: {i+1}")
        found = True
        break

if not found:
    print(f"'{char}' not found in string")


# Short and optimized snippet:

# substring = input("Enter the character or substring to search for: ")

# index = st.find(substring)

# if index != -1:
#     print(f"'{substring}' found in string at index: {index} and position: {index + 1}")
# else:
#     print(f"'{substring}' not found in the string.")
