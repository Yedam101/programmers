def solution(keyinput, board):
    v = board[0]//2
    h = board[1]//2
    
    vnum, hnum = 0, 0

    for i in keyinput:
        if i[0] == 'l' and vnum > -v:
            vnum -= 1
        elif i[0] == 'r' and vnum < v:
            vnum += 1
        elif i[0] == 'u' and hnum < h:
            hnum += 1
        elif i[0] == 'd' and hnum > -h:
            hnum -= 1
    return [vnum, hnum]
    