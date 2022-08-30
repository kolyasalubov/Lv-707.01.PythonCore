from math import factorial


number = int(input("Введите число :"))
factoriall = 1
for i in range(2, number + 1):
    factoriall *= i
print(f'Факториал числа {number} = {factoriall}')