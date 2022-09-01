class Human:
    
    SPECIES = "Homosapiens"

    @classmethod
    def returnInfo(cls):
        if cls.SPECIES:
            return "You belong to the species 'Homosapiens.'"

    def __init__(self, name):
        self.name = name

    def greetMessage(self):
        return f"Hello {self.name}!"
    
    @staticmethod
    def returnSomething():
        return "The human is a social being, possessing reason and consciousness."


h1 = Human("Ben")
print(h1.greetMessage())
print(Human.returnInfo())
print(Human.returnSomething())
