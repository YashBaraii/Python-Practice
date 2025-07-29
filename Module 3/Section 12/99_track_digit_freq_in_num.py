# Create a dictionary to track frequency of digits in a number.


def track_freq(num):
    dict = {}
    st_num = str(num)
    for ch in st_num:
        if int(ch) in dict:
            dict[int(ch)] += 1
        else:
            dict[int(ch)] = 1

    return dict


num = int(input("\nEnter the number: "))

digit_freq = track_freq(num)
print("Digits frequency in ", num, " are as follows: \n")
for k, v in digit_freq.items():
    print(f"Digit {k} appears {v}x times.")
