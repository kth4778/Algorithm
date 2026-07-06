from collections import deque

def solution(cards1, cards2, goal):
    que1 = deque()
    que2 = deque()
    que3 = deque()
    
    for i in cards1:
        que1.append(i)
        
    for i in cards2:
        que2.append(i)
        
    for i in goal:
        que3.append(i)
        
    while que3:
        word = que3.popleft()
        
        if que1 and que1[0] == word:
            que1.popleft()
        elif que2 and que2[0] == word:
            que2.popleft()
        else:
            return "No"
        
    return "Yes"