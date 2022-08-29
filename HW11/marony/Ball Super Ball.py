class Ball():
    '''
    This is class Ball
    '''
    def __init__(self, ball_type='regular'):
        self.ball_type=ball_type
        
ball1 = Ball()
#ball2 = Ball("super")
ball1.ball_type  #=> "regular"
#ball2.ball_type  #=> "super"