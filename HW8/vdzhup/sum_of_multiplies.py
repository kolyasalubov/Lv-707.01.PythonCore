def sum_multiples(num):
    count = 0
    if num == 0:
        return 0
    for item in range(num):
        if item % 3 == 0 or item % 5 == 0:
            count += item
    return count


print(sum_multiples(6))
print(sum_multiples(16))
print(sum_multiples(15))
