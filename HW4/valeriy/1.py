d = range(1,11)
for i in d:
    if i %2 ==0:
        print("Even numbers that are divisible by 2: " ,i)
    # if i % 3 != 0:
    #     print(i)

d = range(1,11)
for i in d:
    if i %3 ==0:
        print("Even numbers that are divisible by 3: " ,i)

max_num = 10
n = 1
 
while n <= max_num:
    if n % 2 != 0 and n % 3 != 0:
        print("Numbers that are not divisible by 2 and 3: ", n)
    n = n+1