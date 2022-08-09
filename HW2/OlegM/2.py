value_int = int(input('Enter 4-digit number:'))

v_int = value_int

multi = 1
while True:
    multi *= v_int % 10
    v_int = v_int // 10
    if v_int // 10 == 0:
        multi *= v_int
        break
print(f"Multiplication of digits = {multi}")

v_int = value_int
print(f"Revers of number = {str(v_int)[::-1]}")

print(f"Sorted of number = {''.join(sorted(str(v_int)))}")
