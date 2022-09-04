class Employee():
    """
    This class is about the employee's information
    """

    counter=0
    def __init__(self, name, salary):
        Employee.counter +=1
        self.__name = name
        self.__salary = salary
    def __del__(self):
        Employee.counter -=1    

    def total_employee(self):
        return Employee.counter

    def employee_info(self):
        print(f"Name of employee is {self.__name} and his or her salary is {self.__salary}")    



m1 = Employee('Vasya', 200)        
m2 = Employee('Katya', 300)
print(Employee.counter)
m1.employee_info()
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)