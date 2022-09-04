class UserException(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else "Error!"

    def __str__(self):
        return self.message


class Day:
    _dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    def __init__(self, day):
        if self.verify_day(day):
            self.day = int(day)

    def __str__(self):
        return f"{self.day}th day is {self._dict.get(self.day%7)}"

    @staticmethod
    def verify_day(day):
        try:
            day = int(day)
        except Exception:
            raise UserException('Your enter non integer value! Need only integer number more 7')
        if int(day) < 8:
            raise UserException('Your enter day numbers less 8! Need more 7')
        else:
            return True


day_in = input()
try:
    day = Day(day_in)
    print(day)
except UserException as e:
    print(e)
