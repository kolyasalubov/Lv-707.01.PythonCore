n = int(input("Enter required number of Fibonacci sequence elements: "))
list_of_FibNumb=[0,1]
for i in range (2,n):
    list_of_FibNumb.append(list_of_FibNumb[i-2]+list_of_FibNumb[i-1])
print(list_of_FibNumb)
