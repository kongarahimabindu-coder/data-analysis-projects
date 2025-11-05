# 1. Declare and assign the variables here:
shuttle_name = 'Determination'
shuttle_speed_mph = 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 384400
MILES_PER_KM = 0.621

print(shuttle_name)
print(shuttle_speed_mph)
print(distance_to_mars_km)
print(distance_to_moon_km)
print(MILES_PER_KM)

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_mars_km))
print(type(distance_to_moon_km))
print(type(MILES_PER_KM))

# Code your solution to exercises 3 and 4 here:
distance_to_mars_km = 225000000  
MILES_PER_KM = 0.621 
# calculate miles to mars
miles_to_mars = distance_to_mars_km * MILES_PER_KM
print("Miles to Mars:", miles_to_mars)

shuttle_speed_mph = 17500
# calculate hours to reach mars
hours_to_mars = miles_to_mars / shuttle_speed_mph
print("Hours to reach Mars:", hours_to_mars)

# calculate days to mars
days_to_mars = hours_to_mars / 24
print("Days to reach Mars:", days_to_mars)

# Print out the results of calculations
shuttle_name = 'Determination'
print(f"{shuttle_name} will take {days_to_mars} days to reach Mars.")

# Code your solution to exercise 5 here

miles_to_moon = distance_to_moon_km * MILES_PER_KM
hours_to_moon = miles_to_moon / shuttle_speed_mph
days_to_moon = hours_to_moon / 24
print(f"{shuttle_name} will take {days_to_moon} days to reach the Moon.")
