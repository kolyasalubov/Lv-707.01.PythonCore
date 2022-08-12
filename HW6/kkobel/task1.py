list_numbers_that_divisible_by_2 = [number for number in range(1,10) if number %2 == 0]
print(f"Numbers that divisible by 2: {list_numbers_that_divisible_by_2}")
list_numbers_that_divisible_by_3 = [number for number in range(1,10) if number %3 == 0 and number %2 != 0]
print(f"Numbers that divisible by 3: {list_numbers_that_divisible_by_3}")
list_numbers_that__are_not_divisible_by_2_and_3 = [number for number in range(1,10) if number %2 != 0 and number %3 != 0]
print(f"Numbers that are not divisible by 2 and 3: {list_numbers_that__are_not_divisible_by_2_and_3}")

list_numbers_that_divisible_by_2 = []
list_numbers_that_divisible_by_3 = []
list_numbers_that__are_not_divisible_by_2_and_3 = []

for number in range(1,10):
    if number %2 == 0:
        list_numbers_that_divisible_by_2.append(number)    
    elif number %3 == 0 and number %2 !=0:
        list_numbers_that_divisible_by_3.append(number)
    elif number %2 != 0 and number %3 != 0:
        list_numbers_that__are_not_divisible_by_2_and_3.append(number)    

print(f"Numbers that divisible by 2: {list_numbers_that_divisible_by_2}")
print(f"Numbers that divisible by 3: {list_numbers_that_divisible_by_3}")
print(f"Numbers that are not divisible by 2 and 3: {list_numbers_that__are_not_divisible_by_2_and_3}")                 
