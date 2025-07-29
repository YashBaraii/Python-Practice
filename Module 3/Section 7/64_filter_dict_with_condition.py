# Filter out key-value pairs where value < 50


def filter_dict(dt):
    filtered_dt = {k: v for k, v in dt.items() if v <= 50}
    remaining_dt = {k: v for k, v in dt.items() if v > 50}
    return filtered_dt, remaining_dt


dt = {0: 0, 1: 20, 2: 40, 3: 60, 4: 80, 5: 100}

print("\nOriginal unfiltered dict: ", dt)

dt, filtered_dt = filter_dict(dt)
print("\nDict after filteration: ", dt)
print("\nFiltered out dict: ", filtered_dt)
