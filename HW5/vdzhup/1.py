user_count_of_number = int(input("How many numbers you want to enter: "))

integer_list = [int(input(f"Enter your {item + 1} number: ")) for item in range(user_count_of_number)]
float_list = [float(item) for item in integer_list]

print(f"Before change: {integer_list}, after change: {float_list}")
