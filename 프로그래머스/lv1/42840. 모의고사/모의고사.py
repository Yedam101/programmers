def solution(answers):
    
#     one = [1, 2, 3, 4, 5]*2000
#     two = [2, 1, 2, 3, 2, 4, 2, 5]*1250
#     thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    
#     i = 0
#     C1, C2, C3 = 0, 0, 0 
#     result = []
#     while i < len(answers):
#         if answers[i] == one[i]:
#             C1 += 1
#         if answers[i] == two[i]:
#             C2 += 1       
#         if answers[i] == thr[i]:
#             C3 += 1   
#         i += 1
    
#     m = max(C1, C2, C3)
    
#     if m == C1:
#         result.append(1)
#     if m == C2:
#         result.append(2)  
#     if m == C3:
#         result.append(3)
        
#     return result
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
        
        
    