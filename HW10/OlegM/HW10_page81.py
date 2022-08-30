from pprint import pprint
import random


class Employee():
    '''
    Class Employee. Base information about name and salary of employs
    '''
    __counter = 0

    def __new__(cls, *args, **kwargs):
        cls.__counter += 1
        return super().__new__(cls)

    def __init__(self, name='No_name', salary = 0):
        self._name = name
        self._salary = salary

    def __del__(self):
        Employee.__counter -= 1

    def show_info_empl(self):
        print(f"Person: {self.name} Salary {self.salary}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name != '':
            self._name = name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, (int, float)) and salary >= 0:
            self._salary = salary

    @classmethod
    def show_count(cls):
        print(f"total number of employees: {cls.__counter}")

    @classmethod
    def show_class_information(cls):
        print("\n---------class information-------")
        print(f"Наслідуваня класів: {cls.mro()}")
        print(f"Назва класу: {cls.__name__}")
        print("Простір імен класу:")
        pprint(cls.__dict__)
        print(f"Назва модулю: {cls.__module__}")
        print(f"Опис класу: {cls.__doc__}")




lst_employess = []
for i in range(15):
    name = random.choice(['Oliver', 'Jake', 'Noah',	'James', 'Connor', 'Liam', 'John'])
    salary = random.randint(10000, 20000)
    lst_employess.append(Employee(name, salary))

lst_employess[0].show_count()

[lst_employess[i].show_info_empl() for i in range(len(lst_employess))]

lst_employess[0].show_class_information()
