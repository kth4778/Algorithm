def solution(t, p):
    answer = 0
    
    len1 = len(t)
    len2 = len(p)
    
    for i in range(len1 - len2 + 1):
        if int(t[i: i + len2]) <= int(p):
            answer += 1
    
    return answer