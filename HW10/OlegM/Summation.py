def summation(num: int) -> int:
    return sum(i for i in range(num + 1))


num = 12
print(f"Аmount of every number from 1 to {num}: {summation(num)}" if str(num).isdigit() else f"Enter value mast be positive integer")
