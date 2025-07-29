# Accept an amount in rupees and break it into currency notes (100s, 50s, 10s, 1s).


def convert1(amt):
    hundreds = amt // 100
    print("100 x", hundreds)
    remaning = amt - (hundreds * 100)

    fifties = remaning // 50
    print("50 x", fifties)
    remaning = remaning - (fifties * 50)

    tens = remaning // 10
    print("10 x", tens)
    remaning = remaning - (tens * 10)

    ones = remaning
    print("1 x", ones)


def convert2(amt):
    denominations = [500, 100, 50, 20, 10, 1]

    for note in denominations:
        count = amt // note
        print(f"{note} notes x {count}")
        amt %= note


num = int(input("\nEnter the amount (₹): "))
convert2(num)
