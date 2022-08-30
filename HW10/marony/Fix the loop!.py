def list_animals(animals):
    final_list=''
    counter=0
    nl='\n'
    for i in (animals):
        counter+=1
        final_list += f'{counter}. {i}{nl}'
    print (final_list)
list_animals() #insert your list here