def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg*fuel_left >= distance_to_pump





a=zero_fuel(int(input("Enter the distance you have to cross")), int(input("\nEnter the everage fuel using")), int(input("\nEnter the volume of fuel left")))
print(a)

