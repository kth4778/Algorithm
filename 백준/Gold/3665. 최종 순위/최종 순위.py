from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    l = list(map(int,input().split()))
    m = int(input())
    graph = [[] for _ in range(N + 1)]
    count = [0 for _ in range(N + 1)]
    result = []
    que = deque()
    switch = True

    for i in range(N):
        for j in range(i + 1, N):
                graph[l[i]].append(l[j])
                count[l[j]] += 1

    for _ in range(m):
        a,b = map(int,input().split())
        if b in graph[a]:
            graph[a].remove(b)
            count[b] -= 1
            graph[b].append(a)
            count[a] += 1
        else:
            graph[b].remove(a)
            count[a] -= 1
            graph[a].append(b)
            count[b] += 1
            
    for i in range(1, N + 1):
        if count[i] == 0:
            que.append(i)

    while que:
        p = que.popleft()
        result.append(p)

        if que:
            switch = False
            break

        for i in graph[p]:
            count[i] -= 1
            if count[i] == 0:
                que.append(i)
    
    if not switch:
        print("?")
    elif len(result) != N:
        print("IMPOSSIBLE")
    else:
        print(*result)