import re
password=input('Enter your password: ')
pattern='^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[$#@]).{6,16}$'
if re.fullmatch(pattern, password):
  print('Congrats! There is a match.')
else:
  print('Wrong password')