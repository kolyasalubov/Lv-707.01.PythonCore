import random
a=random.randint(1,100)
print("Компютер задумав число. Відгадай його ")
k=1
n=int(input("Введи власне число "))
while n!=a:
    if n<a:
        print("Ваше число менше")
        k=k+1
    if n>a:
        print("Ваше число більше")
        k=k+1
    if n==a:
        print("Ви вгадали")
        k=k+1
    n=int(input("Введи власне число "))
print("Ви вгадали за ",k," спроб")    
