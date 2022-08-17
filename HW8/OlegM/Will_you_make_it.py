def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    # is possible to get destination
    return True if mpg * fuel_left >= distance_to_pump else False


print(zero_fuel(10, 2, 4))
