'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:
'''


def are_you_playing_banjo(name: str):
    return name + ' plays banjo' if name[0].lower() == 'r' or name[0].upper() == 'R'  else name + ' does not play banjo'

user_input = are_you_playing_banjo(input('Enter your name: '))
print(user_input)
