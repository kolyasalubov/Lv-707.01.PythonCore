n = int(input("Enter a number for fibonacci formula:"))

i = 1
fib1 = 0
fib2 = 1

for i in range(1, n):
    if i > 0:
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        print("fib numbers are",fib, end = ' ')
else:
    if n == 0:
        print("fib number is 0")
# I couldn't make it work with the following construction print(f"fib number is {n}" if n == 0 else f" fib number is {fib}")    
