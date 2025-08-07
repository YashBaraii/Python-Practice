# Write a closure to remember last n inputs.


def last_n_inputs(n):
    inputs = []

    def remember(input):
        inputs.append(input)
        return inputs[-n:]

    return remember


remember = last_n_inputs(5)

print(remember(10))
print(remember(20))
print(remember(30))
print(remember(40))
