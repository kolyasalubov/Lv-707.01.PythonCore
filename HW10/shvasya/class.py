class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return "Hello user {self.name}"   

    @classmethod
    def methodClass(cls):
        return "this class is homosapines,", cls

    @staticmethod
    def any_message():
        return "I hope I can become a coder"    