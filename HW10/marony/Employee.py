import gc
class Employee():
    """
This is Employee class.
    """
    counter=0
    def __init__(self, name, salary):
        Employee.counter+=1
        self.name=name
        self.salary=salary
    def __del__(self):
        Employee.counter-=1
    def infoPerson(self):
        print(f'Employee name is: {self.name}, employee salary is: {self.salary}')
    @classmethod
    def counterPrint (cls):
        print (f'Total number of employees: {cls.counter}')
    @classmethod
    def infoAll(cls):
        for obj in gc.get_objects():
            if isinstance(obj, cls):
                print(f'Employee name is: {obj.name}, employee salary is: {obj.salary}')


    
a1 = Employee('Jack', 150)
a2 = Employee('Kate', 300)
a3 = Employee('Ann', 200)

Employee.counterPrint()
Employee.infoAll()

print("Base classes from which the employee class is inherited:", Employee.__base__)
print("Class namespace: ", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name in which the class is defined:", Employee.__module__)
print("Documentation bar:", Employee.__doc__)
