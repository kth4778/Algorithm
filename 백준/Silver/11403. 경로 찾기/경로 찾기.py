from collections import deque

n=int(input())
result=[[] for _ in range(n)]

for i in range(n):
    t=list(map(int,input().split()))
    for w in range(n):
        if t[w]==1:
            result[i].append(w)

for i in range(n):
    que=deque()
    que.append(i)
    visited=[False for _ in range(n)]
    while que:
        a=que.popleft()
        for w in result[a]:
            if not visited[w]:
                que.append(w)
                visited[w]=True
                if w not in result[i]:
                    result[i].append(w)
answer=[['0' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for w in result[i]:
        answer[i][w]='1'
for i in answer:
    print(' '.join(i))