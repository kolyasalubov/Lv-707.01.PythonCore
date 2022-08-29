import random


class Ghost:
    def __init__(self):
        self._color = random.choice(("white", "yellow", "purple", "red"))

    @property
    def color(self):
        return self._color


ghost = Ghost()
print(ghost.color)
