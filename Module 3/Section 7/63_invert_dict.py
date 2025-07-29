# Invert a dictionary (keys → values, values → keys).

d1 = {1: 1, 2: 4, 3: 9, 4: 16}

print(f"\n Original Dict: {d1}")

inverted = {value: key for key, value in d1.items()}

print(f"Inverted Dict: {inverted}")
