from collections import deque

n=int(input())
x,y=map(int,input().split())
m=int(input())

count=-1
maps=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
que=deque()
que.append([x,0])

for _ in range(m):
    a,b=map(int,input().split())
    maps[b].append(a)
    maps[a].append(b)


while que:
    idx,cost=que.popleft()
    visited[idx]=True
    if idx==y:
        count=cost
        break
    
    for i in maps[idx]:
        if not visited[i]:
            que.append([i,cost+1])
print(count)