# Task 6.1

tuple_even = [item for item in range(10) if item % 2==0] 
tuple_odd = [item for item in range(10) if item % 3 ==0 and item % 2] 
tuple_not_devisible_2_3 = [item for item in range(10) if item % 2 and item % 3] 

print("Even numbers that are divisible by 2: ", tuple_even)
print("Odd numbers, which are divisible by 3: ",tuple_odd)
print("Numbers that are not divisible by 2 and 3: ", tuple_not_devisible_2_3)