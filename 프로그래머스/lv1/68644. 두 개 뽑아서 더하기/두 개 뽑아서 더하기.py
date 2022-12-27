from itertools import combinations
def solution(numbers):
    a = list(combinations(numbers, 2))
    ans = [sum(i) for i in a]
    
    return sorted(list(set(ans)))