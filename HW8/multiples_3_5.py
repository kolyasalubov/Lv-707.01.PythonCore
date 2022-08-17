def solution(number):
    sum = 0
    if number <0:
        return sum
    else:
        for a in range(1, number):
            if a%3==0 or a%5==0:
                sum+=a
        return sum
print(solution(12))