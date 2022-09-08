class Human(object):
    pass
class Man(Human):
    def __init__(self):
        super().__init__()
class Woman(Human):
    def __init__(self):
        super().__init__()
def God():
    first_man = Man()
    first_woman = Woman()
    people = [first_man, first_woman]
    return people
people = God()
print(isinstance(people[0], Man))