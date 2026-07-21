from collections import deque
import copy

def solution(message, spoiler_ranges):
    answer = 0
    que = deque()
    cur_message = list(message)

    for i in spoiler_ranges:
        que.append(i)
        for j in range(i[0], i[1] + 1):
            if cur_message[j] != ' ':
                cur_message[j] = '!'
    d = {}
    
    for s in (''.join(cur_message)).split():
        if '!' not in s:
            d[s] = True
    
    while que:
        s, e = que.popleft()
        new_message = copy.deepcopy(cur_message)
        
        for i in range(s, e + 1):
            new_message[i] = message[i]
        
        cur = [s for s in (''.join(cur_message)).split() if '!' not in s]
        new = [s for s in (''.join(new_message)).split() if '!' not in s]
        
        p = []
        
        for i in new:
            if i in cur:
                cur.remove(i)
            else:
                p.append(i)
        
        for i in p:
            if i not in d:
                answer += 1
                d[i] = True
                
        cur_message = new_message
    return answer