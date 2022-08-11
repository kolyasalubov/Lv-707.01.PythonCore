even_number_divisible_by_two = []
odd_numbers_divisible_by_3 = []
numbers_that_are_not_divisible_by_2and_3 = []
for a in range(1,int(input("Enter some number"))):
    if a%2 ==0:
        even_number_divisible_by_two.append(a)
    if a%2!=0 and a%3==0:
        odd_numbers_divisible_by_3.append(a)
    if a%2!=0 and a%3 !=0:
        numbers_that_are_not_divisible_by_2and_3.append(a)
    

print(even_number_divisible_by_two)
print(odd_numbers_divisible_by_3)
print(numbers_that_are_not_divisible_by_2and_3)