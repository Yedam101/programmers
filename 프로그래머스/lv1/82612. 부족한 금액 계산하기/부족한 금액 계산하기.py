def solution(price, money, count):
    if money - sum([price*i for i in range(1, count +1)]) >= 0:
        return 0
    else:
        return -(money - sum([price*i for i in range(1, count +1)]))
