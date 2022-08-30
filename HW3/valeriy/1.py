n = int(input("Enter your number:" ))
factor = 1
 
for i in range(1, n+1):
    factor *= i
 
print(factor)