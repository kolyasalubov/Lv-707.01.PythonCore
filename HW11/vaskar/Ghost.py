import random
colors = ['red', 'white', 'yellow', 'purple']
class Ghost(object):
    def __init__(self):
        self.color = random.choice(colors)