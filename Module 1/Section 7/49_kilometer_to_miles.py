# Convert kilometers to miles.

# 1km = 0.621371 miles
# 1mile = 1.60934 km


km_to_miles = lambda km: km * 0.621371
miles_to_km = lambda miles: miles * 1.60934

dist = float(input("\nEnter the distance (km): "))
print(f"Its conversion into miles: {km_to_miles(dist):.5f}")

dist2 = float(input("\nEnter the distance (miles): "))
print(f"Its conversion into kilometers: {miles_to_km(dist2):.5f}")
