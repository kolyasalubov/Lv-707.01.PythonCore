class Employee:
    '''
    Create an employee class. Each employee has
    characteristics such as name and salary. The class should
    have a counter that calculates the total number of
    employees, as well as a method that prints the total
    number of employees and a method that displays
    information about each employee in particular, namely
    the name and salary.
    In addition to creating a class, display information about
    the base classes from which the employee class is
    inherited (__base__), the class namespace (__dict__),
    the class name (__name__), the module name in which
    the class is defined (__module__), the documentation
    bar ( __doc__)
    '''
    count = 0
    def __init__(self, name: str, salary: int):
        Employee.count += 1
        self.name = name
        self.salary = salary
   

    def count_of_employees(self):
        return f"Amout of employees are: {self.count}"

    def info_of_employee(self):
        return f"Hello dear {self.name}. Your salary is: {self.salary}"   

employee1 = Employee('Andrii', 100)
employee2 = Employee('Ivan', 100)
employee3 = Employee('Maks', 100)
employee4 = Employee('Oleksandr', 200)

print(employee1.count_of_employees())

print('Base of Class is:', Employee.__base__)
print('Name of Class is:', Employee.__name__)
print('Dict of Class is:', Employee.__dict__)
print('Module of Class is:', Employee.__module__)
print('Doc string of Class is:', Employee.__doc__)

print('Module of instance is:', employee1.__module__)
print('Doc string of instance is:', employee1.__doc__)
print("Dict of instance is:", employee1.__dict__)

print(employee1.info_of_employee())
print(employee2.info_of_employee())
print(employee3.info_of_employee())
