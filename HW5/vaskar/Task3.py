iterations = int(input("How many iterations do you want?"))
start = 0
initial = 1
iters = 1
#iterations for advanced users
if iterations == 0:
    print("You know what, you do know what Fibonacci sequence is. Stop playing with our expensive software \
        and enter number of iterations >0 in natural numbers")
else:
    while iters <=iterations:
        fibo = start + initial
        start = initial
        initial = fibo
        print(fibo)
        iters +=1
# up to some number
end = int(input("Up to what number would you like to calcilate Fibonacci sequense?"))
start = 0
initial = 1
fibo = 0
while fibo <=end:
    fibo = start + initial
    start = initial
    print(initial)
    initial = fibo