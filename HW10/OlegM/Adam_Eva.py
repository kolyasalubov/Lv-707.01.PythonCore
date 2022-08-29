class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name='Adam'):
        super(Man, self).__init__(name)


class Woman(Human):
    def __init__(self, name='Eva'):
        super(Woman, self).__init__(name)


def god() -> list:
    return [Man(), Woman()]


print(god()[0].name)
print(god()[1].name)
