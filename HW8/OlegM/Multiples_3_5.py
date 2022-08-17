def solution(number: int) -> int:
        '''
        :param number:
        :return: sum of list of numbers multiply 3 and 5 below number
        '''
        return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0]) if number > 0 else 0


print(solution(16))
