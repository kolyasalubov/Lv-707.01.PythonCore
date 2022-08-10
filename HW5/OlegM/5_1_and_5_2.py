# First part. Transform from int to float
lst = [int(x) for x in input("Enter elements of integer type use space between elements:").split()]
for x in range(len(lst)):
    lst[x] = float(lst[x])
print("Transform list:", *lst)

# Second part. Print Fibonacci numbers
n = int(input("Enter number N for calculate Fibonacci numbers:"))
lst_f = []
for i in range(0, n + 1):
    if i < 2:
        lst_f.append(i)
    else:
        lst_f.append(lst_f[i - 1] + lst_f[i - 2])
print(f"List of Fibonachi, {len(lst_f)} elements:", *lst_f)
