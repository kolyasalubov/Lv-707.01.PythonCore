def char_counter(string):
    """This function gets a string and transform it to dict
    with the number of each symbol in this string on the place of value of the dict
    """
    my_dict = {i: list(string).count(i) for i in list(string)}
    print (my_dict)

char_counter(input("Enter your string: "))