def filter_words(st):
    list_of_words = st.lower().split()
    list_of_words[0]=list_of_words[0].title() 
    final_string=''
    for i in list_of_words:
        final_string= final_string+i +' '
    print ('Filtered string:', final_string.strip())
    
filter_words(input('Enter your string: '))