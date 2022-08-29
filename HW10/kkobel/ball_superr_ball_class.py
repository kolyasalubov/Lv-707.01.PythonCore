class Ball:
    '''
    Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
    If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
    '''
    def __init__(self, type='regular') -> None:
        self.ball_of_type = type

    def ball_type(self):
        return self.ball_of_type

ball1 = Ball()
ball2 = Ball('super')
print(ball1.ball_type())
print(ball2.ball_type())
