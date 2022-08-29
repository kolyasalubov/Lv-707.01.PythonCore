def double_char(s):
    characters = [x for x in s]
    doublestring=''
    for char in characters:
        doublestring+=char*2
    print(doublestring)     
double_char(input())