class UserException(BaseException):
    def __init__(self, *args):
        self.message = args[0] if args else "Error!"

    def __str__(self):
        return self.message


class Age:
    def __init__(self, age):
        if self.verify(age):
            self.age = int(age)

    def __str__(self):
        return 'Your age is even.' if self.age % 2 == 0 else 'Your age is odd.'

    @staticmethod
    def verify(age):
        try:
            age = int(age)
        except ValueError:
            raise UserException('Your enter non integer value!')
        if int(age) <= 0:
            raise UserException('Your enter negative value or 0!')
        else:
            return True


while (age_in := input('Enter your age or "0" for exit:')) != '0':
    try:
        age = Age(age_in)
        print(age)
    except UserException as e:
        print(e)

