# Task 2
number = int(input("Input fibonacci value: "))
n = 1
fibonacci = [0, 1]

while fibonacci[n] + fibonacci[n - 1] <= number:
    fibonacci.insert(n + 1, fibonacci[n] + fibonacci[n - 1])
    n += 1

print(f"Fibonacci list {fibonacci}")