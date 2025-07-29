# Break the loop when number > 100 is entered.


def loop():
    i = 1
    while True:
        if i > 100:
            break
        print(i, end=" ")
        i += 1


loop()
