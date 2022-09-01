def summation(num: int) -> int:
    count_sum = 0

    for item in range(num + 1):
        count_sum += item
    return count_sum


print(summation(8))
print(summation(22))
