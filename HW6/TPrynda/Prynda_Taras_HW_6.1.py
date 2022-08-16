list=range(1,10)


for i in list:
    if i%2==0:
        print(f"Number {i} - is EVEN number divisible by 2")
    


for i in list:
    
    if i%3==0 and i%2>0:
        print(f"Number {i} - is ODD number divisible by 3")
    
for i in list:
    
    if i%3>0 and i%2>0:
        print(f"Number {i} - is not divisible by 2 and 3")