from collections import deque
ladder,snake=map(int,input().split())
maps=[i for i in range(101)]
for _ in range(ladder):
    a,b=map(int,input().split())
    maps[a]=b
for _ in range(snake):
    a,b=map(int,input().split())
    maps[a]=b

visited=[False for i in range(101)]
que=deque()
que.append([1,0])
visited[1]=True
while que:
    idx,cost=que.popleft()
    if idx==100:
        print(cost)
        break
    for i in maps[idx+1:idx+7]:
        if not visited[i]:
            que.append([i,cost+1])
            visited[i]=True