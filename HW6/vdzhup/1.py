first_list = [item for item in range(1, 10) if item % 2 == 0]
print(f"Even numbers that are divisible by 2 in range from 1 to 10: {first_list}")

second_list = [item for item in range(1, 10) if item % 2 != 0 and item % 3 == 0]
print(f"Odd numbers, which are divisible by 3 in range from 1 to 10: {second_list}")

third_list = [item for item in range(1, 10) if item % 2 != 0 and item % 3 != 0]
print(f"Numbers that are not divisible by 2 and 3 in range from 1 to 10: {third_list}")
