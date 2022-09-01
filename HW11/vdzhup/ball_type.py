class Ball:
    
    def __init__(self, ball_type = "regular"):
        self._ball_type = ball_type
    
    @property
    def ball_type(self):
        return self._ball_type


ball1 = Ball()
print(ball1.ball_type)

ball2 = Ball("super")
print(ball2.ball_type)
