input_number = (input("Enter a number:"))
conv_number = list(input_number)
multiple = (int(conv_number[0])*int(conv_number[1])*int(conv_number[2])*int(conv_number[3]))
print(f'the result of multiplying of the digits is {multiple}')
# I did with   conv_number.reverse(), but Kostya gave me a clue
print(f'reverse number is {conv_number [::-1]}')
#here I didn't know how to sort without a "sort" function
conv_number.sort()
print(f'sorted numbers are {conv_number}')