letters = {'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'}
upper_letters ={a.upper() for a in letters}
numbers = {'1','2','3','4','5','6','7','8','9','0'}
specials = {'!','@','#','$','%','^','&','*','(',')','_','-'}

user_password = str(input('please create your password:  '))
user_password_set = set(user_password)


if len(user_password_set & letters) > 0 and len(user_password_set & upper_letters) > 0 \
    and len(user_password_set & numbers) > 0 and len(user_password_set & specials) > 0 and \
    len(user_password) < 16 and len(user_password)>6:
    print('Good password - no one will crack it!')
else:
    print('invalid password! improve your password - read the requirements')
    

print(user_password)