class Person:
    '''
    Your task is to complete this Class, the Person class has been created. 
    You must fill in the Constructor method to accept a name as string and an age as number, 
    complete the get Info property and getInfo method/Info getter which should return johns age is 34
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

person1 = Person("John",16)
print(person1.info)

person2 = Person("Matt",25)
print(person2.info)

person3 = Person("Alex",57)
print(person3.info)

person4 = Person("Cam",39)
print(person4.info)   
