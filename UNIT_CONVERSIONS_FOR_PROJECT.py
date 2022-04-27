SPEED_OF_SOUND= 343

def meters_per_second():
    distance_in_meters = SPEED_OF_SOUND
    return distance_in_meters

def centimeters_per_second():
    distance_in_cm = meters_per_second() * 100
    return distance_in_cm

def feet_per_second():
    distance_in_ft = SPEED_OF_SOUND * 1125
    return distance_in_ft

def miles_per_hour():
    distance_in_miles = SPEED_OF_SOUND * 767
    return distance_in_miles

def inches_per_second():
    distance_in_inches = feet_per_second() * 12
    return distance_in_inches


    


def cm_in():
    cm = float(input("Enter a distance in centimeters: "))
    inches = cm / 2.54
    print("Distance in inches:{}".format(inches))

def in_feet():
    inches = float(input("Enter a distance in inches: "))
    feet = inches / 12
    print("Distance in feet:{}".format(feet))

def feet_meters():
    feet = float(input("Enter a distance in feet: "))
    meters = feet / 3.281
    print("Distance in meters:{}".format(meters))

def meter_mile():
    meter = float(input("Enter a distance in meters: "))
    miles = meter / 1609
    print("Distance in miles:{}".format(miles))


print(meters_per_second())

print(centimeters_per_second())

print(feet_per_second())

print(miles_per_hour())

print(inches_per_second())


    
    
