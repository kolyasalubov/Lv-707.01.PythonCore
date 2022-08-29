class Employee():
    __link_class = None
    __counter = 0

    def __new__(cls, *args, **kwargs):
        cls.__counter += 1
        cls.__link_class = super().__new__(cls)
        return cls.__link_class

    def __init__(self, name='Alex', salary=1000):
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.__counter -= 1


    @classmethod
    def show_count(cls):
        print(f"total number of employees: {cls.__counter}")


a = Employee()
a.show_count()

c = Employee()
c.show_count()

b = Employee()
b.show_count()

del a
b.show_count()