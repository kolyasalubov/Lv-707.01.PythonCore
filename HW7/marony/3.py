def numberOfChar(string):
    list_words = string.lower().split()
    list_char = [i[j] for i in list_words for j in range (len(i))]
    dict_count = {i: list_char.count(i) for i in list_char}
    print (dict_count)
numberOfChar(input('Enter your string: '))