'''Task1. In the range from 1 to 10 determine
• even numbers that are divisible by 2,
• odd numbers, which are divisible by 3,
• numbers that are not divisible by 2 and 3.'''

lst_1 = [x for x in range(1, 11) if not x % 2]
print("Even numbers in range 1-10 that are divisible by 2:", *lst_1)

lst_2 = [y for y in range(1, 11) if y % 3 == 0 and y % 2 != 0]
print("Odd numbers in range 1-10 that are divisible by 3:", *lst_2)


print("Numbers in range 1-10 that are not divisible by 2 and 3:", *[z for z in range(1, 11) if z % 3 != 0 and z % 2 != 0])