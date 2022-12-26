import math
def solution(progresses, speeds):

    # 아이디어: math.ceil((100 - 진행)/속도) 새로운 배열 만들기
    # 포인터 인덱스 0 저장 후 count 하고 저장된 인덱스 보다 큰 수 나오면
    # count 새 배열에 저장 count 0으로 한뒤 다시 세기... 시간...?
    
    remains = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))]
    
    stt, end, count = 0, 1, 1
    result = []
    while end < len(remains):
        if remains[stt] >= remains[end]:
            end += 1
            count += 1
        else:
            result.append(count)
            count = 1
            stt = end
            end = stt + 1
    result.append(count)
    return result
            
            
            
        
    
    
    
    
    