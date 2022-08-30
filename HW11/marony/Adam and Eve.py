def God():
    man=Man()
    woman=Woman()
    return [man, woman]
class Human(object):
    pass
class Man(Human):
    def __init__(self):
        super().__init__()
class Woman(Human):
    def __init__(self):
        super().__init__()
paradise = God()
print(isinstance(paradise[0], Man))