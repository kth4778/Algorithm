from collections import deque
import sys
input = sys.stdin.readline

n,k,m = map(int,input().split())

visited = [False for _ in range(n+1)]
hiper = [[] for _ in range(n+m+1)]

for i in range(m):
    stations = list(map(int,input().split()))
    for j in range(k):
        hiper[stations[j]].append(n+i+1)
    hiper[n+i+1] = (stations)

que = deque()
que.append([1,1])
visited[1] = True

while que:
    cost,cur = que.popleft()
    if cur == n:
        print(cost)
        sys.exit()
 
    for i in hiper[cur]:
        for j in hiper[i]:
            if not visited[j]:
                visited[j] = True
                que.append([cost+1,j])
print(-1)