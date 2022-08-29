class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def getinfo(self):
        return f'{self.__name}s age is {self.__age}'


person = Person('Alex', 13)
print(person.getinfo)