fibonachi_number = int(input('Enter Fibonachi number: '))
fibonachi_literal_n1 = 0
fibonachi_literal_n2 = 1

list_of_fibonachi = []
if fibonachi_number < 0:
    print(f"Number of Fibonachi {fibonachi_number} isn't positive and can't be exist")
elif fibonachi_number == 0:
   print(f"Number of Fibonachi is: {fibonachi_number}")
else:
    for element in range(0,fibonachi_number):
        if element == 0:
            fibonachi_literal = fibonachi_literal_n1 + 0
            print(f"Fibonachi literal is: {fibonachi_literal}")
        elif element == 1:
            fibonachi_literal = fibonachi_literal_n1 + fibonachi_literal_n2    
            print(f"Fibonachi literal is: {fibonachi_literal}")
        else:
            fibonachi_literal = fibonachi_literal_n1  + fibonachi_literal_n2
            fibonachi_literal_n1 = fibonachi_literal_n2
            fibonachi_literal_n2 = fibonachi_literal   
            print(f"Fibonachi literal is: {fibonachi_literal}")  
        element += 1
        list_of_fibonachi.append(fibonachi_literal)

print(list_of_fibonachi)    


count = 0

if fibonachi_number < 0:
    print(f"Number of Fibonachi {fibonachi_number} isn't positive and can't be exist")
elif fibonachi_number == 0:
   print(f"Number of Fibonachi is: {fibonachi_number}")
else:
    while count < fibonachi_number:
        if count == 0:
            fibonachi_literal = fibonachi_literal_n1
            print(f"Fibonachi literal is: {fibonachi_literal}")
        elif count == 1:
            fibonachi_literal = fibonachi_literal_n1 + fibonachi_literal_n2
            print(f"Fibonachi literal is: {fibonachi_literal}")
        else:
            fibonachi_literal = fibonachi_literal_n1 + fibonachi_literal_n2
            fibonachi_literal_n1 = fibonachi_literal_n2
            fibonachi_literal_n2 = fibonachi_literal
            print(f"Fibonachi literal is: {fibonachi_literal}")
        count += 1
        list_of_fibonachi.append(fibonachi_literal)

print(list_of_fibonachi)            
