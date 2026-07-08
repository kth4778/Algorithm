def solution(answers):
    def lst_ans(lst, l):
        q = len(lst)
        answer = []
        
        for i in range(l):
            answer.append(lst[i % q])
            
        return answer
    o = len(answers)
    
    a1 = lst_ans([1,2,3,4,5], o)
    a2 = lst_ans([2,1,2,3,2,4,2,5], o)
    a3 = lst_ans([3,3,1,1,2,2,4,4,5,5], o)

    p = [0,0,0]
    
    for i in range(len(answers)):
        if a1[i] == answers[i]:
            p[0] += 1
        if a2[i] == answers[i]:
            p[1] += 1
        if a3[i] == answers[i]:
            p[2] += 1
    
    max_num = max(p)
    result = []
    
    for i in range(3):
        if max_num == p[i]:
            result.append(i + 1)
    
    return result