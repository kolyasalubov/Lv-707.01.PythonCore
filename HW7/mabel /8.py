def greet(name):
    #return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


print(greet("Jonny"))