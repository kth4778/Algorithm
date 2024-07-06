from collections import deque

a,b = map(int,input().split())

visited = [100001 for _ in range(100001)]
que = deque([[a,0]])
visited[a] = 0

while que:
    c,cost = que.popleft()
    if c == b:
        print(visited[c])
        break
    lst = [c*2,c+1,c-1]
    for i in range(3):
        if 0<= lst[i] < 100001:
            if i == 0:
                if visited[lst[i]] > cost:
                    visited[lst[i]] = cost
                    que.append([lst[i],cost])
            else:
                if visited[lst[i]] > cost+1:
                    visited[lst[i]] = cost+1
                    que.append([lst[i],cost+1])