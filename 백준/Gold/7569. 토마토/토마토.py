from collections import deque
m,n,h=map(int,input().split())
maps=[[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        maps[i].append(list(map(int,input().split())))

visited=[[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
que=deque()
dx=[1,0,0,-1,0,0]
dy=[0,1,-1,0,0,0]
dz=[0,0,0,0,1,-1]

for i in range(h):
    for w in range(n):  
        for q in range(m):
            if maps[i][w][q]==1:
                que.append([i,w,q,0])
                visited[i][w][q]=True
            elif maps[i][w][q]==-1:
                visited[i][w][q]=True
days=0
vol=True
while que:
    z,y,x,cost=que.popleft()
    days=max(days,cost)
    for i in range(6):
        nz=z+dz[i]
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and 0<=nz<h and not visited[nz][ny][nx]:
            que.append([nz,ny,nx,cost+1])
            visited[nz][ny][nx]=True
for i in visited:
    for w in i:
        if not all(w):
            vol=False
    if not vol:
        break
if vol:
    print(days)
else:
    print(-1)