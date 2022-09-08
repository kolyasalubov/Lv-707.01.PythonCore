import re
password = str(input('Please enter your password: '))
if re.findall("[a-z]", password) and re.findall("[A-Z]", password) and re.findall("[0-9]", password) and \
    len(password) <16 and len(password) > 6 and re.findall("[!, @, #, $, %, ^,&,*,]", password):
    print('Good password')
else:
    print("Improve the password")