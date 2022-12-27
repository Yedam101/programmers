from collections import Counter
import re
def solution(s):
    n = Counter(re.findall('\d+', s))
    ans = list(map(int, [int(i) for i, j in sorted(n.items(), key=lambda x: -x[1])]))
    return ans
    
    
    
    
    
    
#     s = s.replace('{','.').replace('}','.').replace('..','')
#     n = s.split('.,.')
#     n = sorted(n, key=len)
#     m = [i.split(',') for i in n]
#     stack = []
    
#     for i in m:
#         for j in range(len(i)):
#             if i[j] not in stack:
#                 stack.append(i[j])
#     result = [int(i) for i in stack]

#     return result