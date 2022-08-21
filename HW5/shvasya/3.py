n = int(input("Enter a number for fibonacci formula:"))

print(f"fib number is {n}" if n == 0 else "fib numbers are")

i = 1
fib1 = 0
fib2 = 1

for i in range(0, n):
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    print(fib, end = ' ')