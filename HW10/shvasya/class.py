class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Hello user {self.name}"   

    @classmethod
    def methodClass(cls):
        return "this class is homosapines,", cls

    @staticmethod
    def any_message():
        return "I hope I can become a coder"    

s = Human("Vasya")
s.hello
s.any_message
print(s.hello())
print(s.any_message())
print(Human.methodClass())