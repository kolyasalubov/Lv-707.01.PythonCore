my_string = str(input("please enter your string:"))
numerator = {}
def len_func():
    for a in my_string:
        if a in numerator:
            numerator[a] +=1
        else:
            numerator[a] =1
    return numerator
print(len_func())