from collections import deque

n,m,k = map(int,input().split())
maps = [list(map(int,input()))  for _ in range(n)]

que = deque()
que.append([0,0,1,k])
visited = [[[False]*(k+1) for _ in range(m)] for _ in range(n)]
for i in range(k):
    visited[0][0][i]=True
dx = [1,0,0,-1]
dy = [0,1,-1,0]
result = -1

while que:
    y,x,move,times = que.popleft()
    if y == n-1 and x == m-1:
        result = move
        break
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            if times == 0:
                if maps[ny][nx] == 0 and not visited[ny][nx][0]:
                    que.append([ny,nx,move+1,0])
                    visited[ny][nx][0]=True
            else:
                if maps[ny][nx] == 0 and not visited[ny][nx][times]:
                    que.append([ny,nx,move+1,times])
                    visited[ny][nx][times]=True
                elif maps[ny][nx] == 1 and not visited[ny][nx][times-1]:
                    que.append([ny,nx,move+1,times-1])
                    visited[ny][nx][times-1]=True
print(result)