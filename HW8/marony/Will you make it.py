def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump<=mpg*fuel_left
zero_fuel(int(input('Enter distance to pump: ')), int(input('Enter miles per gallon: ')), int(input('Enter fuel you have: ')))