SPEED_OF_SOUND= 343

#conversion for m/s
def meters_per_second():
    distance_in_meters = SPEED_OF_SOUND
    return distance_in_meters

#conversion for cm/s
def centimeters_per_second():
    distance_in_cm = meters_per_second() * 100
    return distance_in_cm

#conversion for foot/s
def feet_per_second():
    distance_in_ft = SPEED_OF_SOUND * 1125
    return distance_in_ft

#conversion for mph
def miles_per_hour():
    distance_in_miles = SPEED_OF_SOUND * 767
    return distance_in_miles

#conversion for inch/s
def inches_per_second():
    distance_in_inches = feet_per_second() * 12
    return distance_in_inches


print(meters_per_second())

print(centimeters_per_second())

print(feet_per_second())

print(miles_per_hour())

print(inches_per_second())


    
    
