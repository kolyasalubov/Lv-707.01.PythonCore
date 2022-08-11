user_fibonacci_number = int(input("Enter the number to create a Fibonacci sequence: "))

fibonacci_list = []
sequnce_result = 1    # 0 1 1 2 3 5 8
count_of_sequence = 0 # 1 1 2 3 5 8 13

for i in range(user_fibonacci_number + 1):
    sequnce_result, count_of_sequence = count_of_sequence, sequnce_result + count_of_sequence
    fibonacci_list.append(sequnce_result)
print(f"Number {user_fibonacci_number} creates the following sequence: {fibonacci_list}")
