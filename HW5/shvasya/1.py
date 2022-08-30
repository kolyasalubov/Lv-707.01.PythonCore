input_number = int(input("Enter a number:"))
fact = 1
i = 0

for i in range(1,input_number + 1):
    fact = fact*i 
print(f"factorial {input_number} = 1" if fact == 0 else f"factorial {input_number} = {fact}")
