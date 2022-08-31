first_string = 3
second_string = 5
print(f"First string was: {first_string}, Second string was: {second_string}")

# One of the variant
first_string, second_string = second_string, first_string
print(f"First string become: {first_string}, Second string become: {second_string}")

# Second of the variant
first_string = first_string + second_string # додаючи 2 змінні ми отримуємо різницю
second_string = first_string - second_string # щоб змінити значення для 2 змінної,ми віднімаємо отримане значення від 2 змінних 15 -5 => 10
first_string = first_string - second_string # А тут віднімаємо вже отримане значення від віднімання отриманої 2 змінної 15 - 10 => 5
print(f"First string become: {first_string}, Second string become: {second_string}")

# Third of the variant
first_string = first_string * second_string 
second_string = int(first_string / second_string) 
first_string = int(first_string / second_string) 
print(f"First string become: {first_string}, Second string become: {second_string}")

# Fourth of variant
first_string = first_string * second_string 
second_string = first_string // second_string 
first_string = first_string // second_string 
print(f"First string become: {first_string}, Second string become: {second_string}")

# Fiveth of variant
first_string = first_string ^ second_string 
second_string = first_string ^ second_string 
first_string = first_string ^ second_string 
print(f"First string become: {first_string}, Second string become: {second_string}")
