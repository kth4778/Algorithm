from collections import deque
import sys
input = sys.stdin.readline

count=0
n,m=map(int,input().split())
visited=[False for _ in range(n+1)]
que=deque([] for _ in range(n+1))

for _ in range(m):
    a,b=map(int,input().split())
    que[a].append(b)
    que[b].append(a)

def bfs(start):
    a=deque([start])
    visited[start]=True
    while a:
        p=a.popleft()
        for i in que[p]:
            if not visited[i]:
                visited[i]=True
                a.append(i)
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        count+=1
print(count)