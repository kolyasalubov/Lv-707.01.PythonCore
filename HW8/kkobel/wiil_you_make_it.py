'''
You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
Considering these factors, write a function that tells you if it is possible to get to the pump or not.
Function should return true if it is possible and false if not.
'''
def zero_fuel(distance_to_pump, mpg, fuel_left):
    result_of_distance = distance_to_pump / mpg
    return True if fuel_left > result_of_distance or fuel_left >= result_of_distance else False 


print(f"Result of your pump is: {zero_fuel(50,25,1)}")
print(f"Result of your pump is: {zero_fuel(50,25,2)}")
print(f"Result of your pump is: {zero_fuel(30,25,1)}")
print(f"Result of your pump is: {zero_fuel(30,25,1.2)}")
