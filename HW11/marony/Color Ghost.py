import random
class Ghost(object):
    '''
    This is class Ghost
    '''
    def __init__(self, color=''):
        self.color=random.choice(["white", "yellow", "purple", "red"])
ghost = Ghost()
ghost.color 