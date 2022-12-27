def solution(lottos, win_nums):
    

    n = lottos.count(0)
    m = len(set(lottos) & set(win_nums))

    ans = [7-(m+n), 7-(m)]
    for i in range(2):
        if ans[i] == 7:
            ans[i] = 6
    return ans
