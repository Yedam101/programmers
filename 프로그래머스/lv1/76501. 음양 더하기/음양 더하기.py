def solution(absolutes, signs):
    sub = [2*(-absolutes[i]) for i in range(len(signs)) if signs[i] == False]

    return sum(absolutes) + sum(sub)