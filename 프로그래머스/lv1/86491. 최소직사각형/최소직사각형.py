def solution(sizes):

    # sdsizes = [sorted(i) for i in sizes]
    # smax = max([sdsizes[i][0] for i in range(len(sdsizes))])
    # lmax = max([sdsizes[i][1] for i in range(len(sdsizes))])
    # return smax*lmax
    

    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
    
