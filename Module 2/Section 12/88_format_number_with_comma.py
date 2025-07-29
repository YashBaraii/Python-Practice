# Format a number with commas using a loop.


def convert(n):
    st_num = str(n)
    l = len(st_num)
    formatted_n_lst = []
    i = 0
    for ch in range(len(st_num) - 1, -1, -1):
        formatted_n_lst.append(st_num[ch])
        i += 1
        if i % 3 == 0 and i != 0:
            formatted_n_lst.append(",")

    return "".join(reversed(formatted_n_lst))


num = int(input("\nEnter the number: "))

formatted_num = convert(num)
print(f"Its comma formatted version is: {formatted_num}")
