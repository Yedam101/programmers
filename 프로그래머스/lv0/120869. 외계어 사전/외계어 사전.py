def solution(spell, dic):
    s = ''.join(spell)
    for i in dic:
        if sorted(i) == sorted(s):
            return 1
    return 2
    
    
    