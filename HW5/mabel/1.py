fib1 = fib2 = 1

number_fibonashi = int(input("Input number: "))
 
 
for otvet in range(2, number_fibonashi ):
    fib1, fib2 = fib2, fib1 + fib2
    
print(f'Otvet: {fib2}')