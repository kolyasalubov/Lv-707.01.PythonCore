import random


class Ghost:
    '''
    Color Ghost
    Create a class Ghost
    Ghost objects are instantiated without any arguments.
    Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
    '''
    colors = ['white', 'yellow', 'purple', 'red']
    def __init__(self) -> None:
        self.color = random.choice(self.colors)

    # Or We can do it as:
    def __init__(self) -> None:
        colors = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(colors)    

    def getting_random_color(self):
        return self.color           

ghost1 = Ghost()
print(f"Random color first object is: {ghost1.getting_random_color()}")

ghost2 = Ghost()
print(f"Random color second object is: {ghost2.getting_random_color()}")
