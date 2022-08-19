user_input_number = int(input('Enter your number: ') )

def solution(user_input_number: int):
    sum_of_numbers = 0
    list_numbers_division_by_3_or_5 = []
    for item in range(1, user_input_number):
        if item %3 == 0 or item %5 == 0:
            sum_of_numbers += item
            list_numbers_division_by_3_or_5.append(item)
        elif item < 0:
            return 0    
    return list_numbers_division_by_3_or_5, sum_of_numbers              

print(f"Result suma of numbers that division by 3 or 5: {solution(user_input_number)}")
