def solution(array, commands):

    answer = []
    for com in commands:
        result = sorted(array[com[0]-1:com[1]])
        answer.append(result[com[2]-1])
        
    return answer