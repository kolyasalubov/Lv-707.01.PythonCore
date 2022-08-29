class Ball:
    def __init__(self, ball_type="regular"):
        self.__ball_type = ball_type

    @property
    def ball_type(self):
        return self.__ball_type


ball = Ball()
print(ball.ball_type)

ball = Ball('Super ball')
print(ball.ball_type)
