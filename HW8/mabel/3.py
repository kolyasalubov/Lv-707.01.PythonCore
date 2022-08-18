def zero_fuel(distance_to_pump, mpg, fuel_left):
    mpg_fuel= mpg*fuel_left
    if distance_to_pump <= mpg_fuel:
        return True
    else:
        return False