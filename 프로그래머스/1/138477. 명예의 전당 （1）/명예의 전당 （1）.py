def solution(k, score):
    answer = []
    lst = []
    
    for i in range(len(score)):
        lst.append(score[i])
        
        if len(lst) > k:
            lst = sorted(lst)[1:]
        
        answer.append(min(lst))
    return answer