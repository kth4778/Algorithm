from collections import deque
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
user=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    user[a].append(b)
    user[b].append(a)
def bfs(p):
    visit=[0 for _ in range(n+1)]
    q=deque()
    q.append(p)

    while q:
        u=q.popleft()
        for i in user[u]:
            if i!=p and not visit[i]:
                q.append(i)
                visit[i] += visit[u]+1
    return sum(visit)

result=[]
for i in range(1,n+1):
    result.append(bfs(i))
print(result.index(min(result))+1)