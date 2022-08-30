def reverse(st):
    list_of_words = [i for i in st.split()]
    reversed_string = ''
    for i in list_of_words[::-1]:
        reversed_string = reversed_string + i + ' '
    print ('Reveresed string:', reversed_string.strip())
reverse(input('Enter your string: '))