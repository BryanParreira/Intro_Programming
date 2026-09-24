def battery_counter(e_dolls, rc_cars, robo_dogs):
    return e_dolls * 2 + rc_cars * 4 + robo_dogs * 6


e_dolls = int(input("How many electronic dolls? "))
rc_cars = int(input("How many remote-controlled cars? "))
robo_dogs = int(input("How many robot dogs? "))
print(battery_counter(e_dolls, rc_cars, robo_dogs))
