def zero_fuel(distance_to_pump, mpg, fuel_left):
    fuel_at_the_end = fuel_left - distance_to_pump/mpg
    if fuel_at_the_end <0:
        return False
    else:
        return True
    #Happy Coding! ;)


print(zero_fuel(50,25,2))