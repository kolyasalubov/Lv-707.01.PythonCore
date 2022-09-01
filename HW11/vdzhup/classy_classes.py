class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def getInfo(self):
        return "%ss age is %d" % (self.name, self.age)

p = Person("john", 34)
print(p.getInfo)
