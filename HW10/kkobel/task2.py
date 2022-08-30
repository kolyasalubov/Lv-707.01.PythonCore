class Human:
    '''
    Create a class Human, everyone has a name, create a
    method in the class that displays a welcome message to a
    each person. Create a class method in the class that
    returns information that it is a species of "Homosapiens".
    And also in the class create a static method that returns
    an arbitrary message
    '''
    def __init__(self,name) -> None:
        self.name = name
    
    def greeting(self):
        return f"Hello dear {self.name} you are in instance method"

    @classmethod
    def class_of_method(cls):
        return "It's kind of Homosapiens",cls
        

    @staticmethod
    def static_of_method():
        return 'Good news for starting some new!'

human1 = Human('Andrii')
print(human1.greeting())
print(human1.class_of_method())
print(Human.class_of_method())  
print(human1.static_of_method())

