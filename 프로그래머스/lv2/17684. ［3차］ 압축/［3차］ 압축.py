def solution(msg):
    dict = {}
    for i in range(65,91):
        dict[chr(i)] = i - 64

    ans = []

    stt = 0
    point = stt + 1
    val = 27

    while point <= len(msg):
        if msg[stt:point] in dict and msg[stt:point+1] not in dict:
            ans.append(dict[msg[stt:point]])
            dict[msg[stt:point+1]] = val
            val, stt, point = max(dict.values())+1, point, stt + 1

        else:
            point += 1
            
    if msg[stt:point-1] in dict:
        ans.append(dict[msg[stt:point-1]])
    else:
        ans.append(max(dict.values())+1)
    
    return ans