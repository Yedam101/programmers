def solution(dartResult):
    dartResult = dartResult + '0'
    dr = []
    start = 0
    for i in range(len(dartResult)):
        if i != 0 and dartResult[i].isdigit() and len(dartResult[start:i]) != 1:
            dr.append(list(dartResult[start:i]))
            start = i

    for i in range(len(dr)):
        if '0' in dr[i] and dr[i].index('0') != 0:
            dr[i][1] = '10'
            dr[i].remove('1')
        if 'S' in dr[i]:
            dr[i][0] = int(dr[i][0])
            dr[i].remove('S')
        elif 'D' in dr[i]:
            dr[i][0] = int(dr[i][0])**2
            dr[i].remove('D')
        elif 'T' in dr[i]:
            dr[i][0] = int(dr[i][0])**3
            dr[i].remove('T')
        if '#' in dr[i]:
            dr[i][0] = -int(dr[i][0])
            dr[i].remove('#') 
        if '*' in dr[i]:
            if i and i != 0:
                dr[i][0], dr[i-1][0] = int(dr[i][0])*2, int(dr[i-1][0])*2
                dr[i].remove('*') 
            else:
                dr[i][0] = int(dr[i][0])*2
                dr[i].remove('*') 

    return sum(sum(dr, [])) 
    
