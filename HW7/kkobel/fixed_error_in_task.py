def greet(name):
    return "Hello, my love!" if name == "Johnny" else "Hello, {name}!".format(name=name)  
   
print(greet('Johnny'))
print(greet('Someone of people'))
