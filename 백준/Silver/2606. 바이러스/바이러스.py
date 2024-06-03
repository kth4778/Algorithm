from collections import deque
n=int(input())
v=int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(v):
    q,w=map(int,input().split())
    graph[q]+=[w]
    graph[w]+=[q]
visited[1]=1
que=deque([1])
while que:
    p=que.popleft()
    for i in graph[p]:
        if visited[i]==0:
            visited[i]=1
            que.append(i)
print(sum(visited)-1)