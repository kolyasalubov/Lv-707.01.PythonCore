a = []
b = []
c = []


for i in range(1, 10):
    if i %3 != 0 and i %2 != 0 :
        a.append(i)
    elif i %3 == 0 and i %2 != 0: 
        b.append(i)
    elif i %2 == 0:
        c.append(i)
    
print(f'Числа которые не деляться на 3 и на 2 {a}')
print(f'Числа которые деляться на 3 {b}')
print(f'Числа которые деляться на 3 {c}')

