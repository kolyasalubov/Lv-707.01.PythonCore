class Human():
    """
This is Human class.
    """
    def __init__(self, name):
        self.name=name
    def greetings(self):
        print(f'Hello, {self.name}!')
    @classmethod
    def species(cls):
        print("Human is Homo sapiens.")
    @staticmethod
    def arbMess():
        print('Carpe diem!')

a=Human(input('Enter your name: '))
a.greetings()
a.species()
a.arbMess()