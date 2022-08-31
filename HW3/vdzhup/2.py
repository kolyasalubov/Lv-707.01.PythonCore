user_num = int(input("Enter a number: "))

fourth_digit = user_num % 10
third_digit = (user_num % 100) // 10
second_digit = (user_num % 1000) // 100
first_digit = user_num // 1000

multiplication = first_digit * second_digit * \
                third_digit * fourth_digit
print(f"Product of digits: {multiplication}")

reverse_oder_digits = int(str(user_num)[::-1])
print(f"Reverse order of digits: {reverse_oder_digits}")

increase_sorted_num = int("".join(sorted(str(user_num))))
print(f"Sorting by increasing: {increase_sorted_num}")
