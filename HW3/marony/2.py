number=str(input('Enter four-digit number: '))

#2.1
mult = int(number[0])*int(number[1])*int(number[2])*int(number[3])
print (mult)

#2.2
rev_number = number[::-1]
print (rev_number)

#2.3
sort_lst = sorted(number)
new_numb = sort_lst[0]+sort_lst[1]+sort_lst[2]+sort_lst[3]
print(new_numb)