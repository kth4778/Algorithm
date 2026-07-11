from collections import deque

def solution(s):
    answer = 0
    que = deque()
    
    for i in s:
        que.append(i)
        
    cur = None
    a1 = 0
    a2 = 0 
    
    while que:
        if cur == None:
            a1 += 1
            cur = que.popleft()
        
        else:
            q = que.popleft()
            if cur == q:
                a1 += 1
            else:
                a2 += 1
        
        if a1 == a2:
            cur = None
            answer += 1
            a1 = 0
            a2 = 0
    if a1 > 0 or a2 > 0:
        answer += 1
    return answer