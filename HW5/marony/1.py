list_of_integers = []
list_of_floats = []
print("Hello! Please enter your numbers for the list.\nAs soon as you are done, enter 'Done'.")
while True:
    i=input('Enter your number: ')
    if i=='Done':
        break
    i=int(i)
    list_of_integers.append(i)

for j in list_of_integers:
    j=float(j)
    list_of_floats.append(j)
print(list_of_floats)