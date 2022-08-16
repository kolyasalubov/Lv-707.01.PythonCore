def greet(name):
    print("Hello, {}!".format(name) if name != "Johnny" else "Hello, my love!")
greet(input('Enter your name: '))