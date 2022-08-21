# Task 1
my_list = [11, 13 , 15, 17, 19]

i = 0
while i < len(my_list):
    my_list[i] = float(my_list[i])
    i += 1

print(f"List {my_list} converted to float.")