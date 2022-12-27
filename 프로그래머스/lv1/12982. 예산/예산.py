def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    else:
        count = 0
        d = sorted(d)
        for i in range(len(d)):
            count += d[i]
            if count > budget:
                return i

    
                