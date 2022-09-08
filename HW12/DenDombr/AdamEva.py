class Person:
    def __init__(self,name,age):
        self.name = name + 's'
        self.age = age
        
    @property
    def info(self):
        return f"{self.name} age is {self.age}"