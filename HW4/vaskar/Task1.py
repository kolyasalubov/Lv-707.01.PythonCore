#Recursion
iterations = int(input("What is your number?"))
result = 1
if iterations ==0 or iterations ==1:
    result = 1
else:
    for a in range(1, iterations+1):
        result*=a

print(result)