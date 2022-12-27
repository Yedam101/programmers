from collections import Counter

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    st1 = []
    st2 = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            st1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            st2.append(str2[i:i+2])        

    inter = list((Counter(st1) & Counter(st2)).elements())
    union = list((Counter(st1) | Counter(st2)).elements())

    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int((len(inter)/len(union))*65536)
