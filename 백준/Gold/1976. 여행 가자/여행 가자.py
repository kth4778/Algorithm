from collections import deque

n = int(input())
m = int(input())
downtown = [[] for _ in range(n+1)]
for i in range(n):
    p = list(map(int,input().split()))
    for w in range(n):
        if i!=w and p[w] == 1:
            downtown[i+1].append(w+1)
rout = list(map(int,input().split()))

def solution(start,end):
    que = deque()
    visited = [False for _ in range(n+1)]
    que.append(start)
    visited[start] = True

    while que:
        node = que.popleft()
        if node == end:
            return True
        for i in downtown[node]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
    return False

switch = True
for i in range(1,m):
    if not solution(rout[i-1],rout[i]):
        switch = False
        break
if switch:
    print("YES")
else:
    print("NO")
