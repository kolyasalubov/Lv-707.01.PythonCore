class Human:
    def __init__(self, name):
        self.name = name
    def welcome(self):
        print("Hello! Nice to meet you!! My name is",  self.name)
    def classmethod(cls):
        return 'Homosapiens', cls
    @staticmethod
    def staticmethod():
        return "let`s do some work, we can: 1. repare a vehicle; 2. mow hay"

vuicko = Human(name = 'Volodymyr')
vuicko.welcome()
print(vuicko.classmethod())
print(vuicko.staticmethod())