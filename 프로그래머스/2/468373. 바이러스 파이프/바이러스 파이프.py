import copy
from collections import deque

def solution(n, infection, edges, k):
    answer = 1
    pipe = [[[] for _ in range(n + 1)] for _ in range(4)]
    
    for x, y, type in edges:
        pipe[type][x].append(y)
        pipe[type][y].append(x)
    
    infections = [False for _ in range(n + 1)]
    infections[infection] = True
    
    que = deque()
    for i in range(1, 4):
        que.append([0, copy.deepcopy(infections), i])
    
    while que:
        k_count, ci, t = que.popleft()
        
        if k_count == k:
            q = 0
            for i in ci:
                if i:
                    q += 1
            answer = max(answer, q)
            continue
            
        d = 0
        while True:
            for virus in range(1, n + 1):
                if ci[virus]:
                    for new_virus in pipe[t][virus]:
                        if not ci[new_virus]:
                            ci[new_virus] = True
                            d += 1
            
            if d == 0:
                break
            else:
                d = 0
                
        for i in range(1, 4):
            que.append([k_count + 1, copy.deepcopy(ci), i])

    return answer