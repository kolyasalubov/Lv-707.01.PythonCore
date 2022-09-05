class Human:
    def __init__(self,name):
        self.name = name
        
class Man(Human):
    def __init__(self):
        super().__init__("Adam")
        
class Woman(Human):
    def __init__(self):
        super().__init__("Eve")
        
def God():
    lst = [Man(),Woman()]
    return lst