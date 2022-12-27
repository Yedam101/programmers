def solution(numbers, k):
    
    lastnum = numbers[-1]
    print(lastnum)
    answer = (2*k-1) % lastnum
    return answer
    
    