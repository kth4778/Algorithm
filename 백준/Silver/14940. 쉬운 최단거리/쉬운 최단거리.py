from collections import deque
n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
start_index=[]
visited=[[False]*m for _ in range(n)]
dx=[1,0,0,-1]
dy=[0,1,-1,0]
que=deque()
for i in range(n):
    if 2 in maps[i]:
        start_index.append(i)
        start_index.append(maps[i].index(2))
        break
que.append([start_index[0],start_index[1],0])
visited[start_index[0]][start_index[1]]=True
maps[start_index[0]][start_index[1]]=0
while que:
    y,x,cost=que.popleft()
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and maps[ny][nx]!=0:
            visited[ny][nx]=True
            que.append([ny,nx,cost+1])
            maps[ny][nx]=cost+1
for i in range(n):
    for w in range(m):
        if not visited[i][w] and maps[i][w]==1:
            maps[i][w]=-1

for i in maps:
    print(' '.join([str(w) for w in i]))