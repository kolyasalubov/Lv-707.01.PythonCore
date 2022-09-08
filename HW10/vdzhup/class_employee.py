class Employees:
    """
    This class describes information about employees, 
    such as salary, employee name, number of employees.
    """

    COUNT_OF_EMPLOYEES = 0

    def __init__(self, name = None, salary = 0):
        self._name = name
        self._salary = salary
        Employees.COUNT_OF_EMPLOYEES += 1

    @classmethod
    def printEmployees(cls):
        return f"Count of employees: {cls.COUNT_OF_EMPLOYEES}"
    
    @property
    def name(self):
        print("getter method 'name' called")
        return self._name
        
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
            print("setter method 'name' called") 

    @property
    def salary(self):
        print("getter method 'salary' called")
        return self._salary
 
    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int):
            self._salary = salary
            print("setter method 'salary' called")
    
    def infoEmployees(self):
        return f"Employee {self._name} has a salary of {self._salary}"

    @classmethod
    def classInfo(cls):
        print(f"The employee class is inherited: {cls.__mro__}")
        print(f"The class namespace: {cls.__dict__}")
        print(f"The class name: {cls.__name__}")
        print(f"The module name in which the class is defined: {cls.__module__}")
        print(f"The documentation bar {cls.__doc__}")


emp1 = Employees()
emp1.name = "Ben"
emp1.salary = 1000
print(emp1.infoEmployees())

emp2 = Employees()
emp2.name = "John"
emp2.salary = 1200
print(emp2.infoEmployees())

emp3 = Employees()
emp3.name = "Greg"
emp3.salary = 800
print(emp3.infoEmployees())

print(Employees.printEmployees())

Employees.classInfo()
