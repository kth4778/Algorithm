from collections import deque

def solution(ingredient):
    answer = 0
    que_L = deque()
    que_R = deque()
    
    for i in ingredient:
        que_R.append(i)
    
    while que_R:
        p = que_R.popleft()
        
        if len(que_L) < 3:
            que_L.append(p)
        elif p == 1:
            a3 = que_L.pop()
            a2 = que_L.pop()
            a1 = que_L.pop()
            if a3 == 3 and a2 == 2 and a1 == 1:
                answer += 1
            else:
                que_L.append(a1)
                que_L.append(a2)
                que_L.append(a3)
                que_L.append(p)
        else:
            que_L.append(p)
            
    if list(que_L)[-4:] == [1,2,3,1]:
        answer += 1
        
    return answer