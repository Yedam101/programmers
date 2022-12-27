from itertools import combinations
def solution(nums):
    even = [i for i in nums if i % 2 == 0]
    odd = [i for i in nums if i % 2 == 1]
    
    oddadd = [sum(i) for i in list(combinations(odd, 3))]
    evenadd = [sum(i) for i in list(combinations(even, 2))]
    ans = []
    for i in evenadd:
        for j in odd:
            ans.append(i+j)
    ans = ans + oddadd
    
            
    count = 0            
    for i in ans:
        check = 0
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                check = -1
        if check == 0:
            count += 1
    return count