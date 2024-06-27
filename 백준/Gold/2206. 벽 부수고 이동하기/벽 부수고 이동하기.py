from collections import deque

n,m = map(int,input().split())
maps = [list(map(int,input())) for _ in range(n)]
dx = [1,0,0,-1]
dy = [0,1,-1,0]
que = deque()
que.append([0,0,1,1])
result = -1
visited = [[[False]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][1]=True
visited[0][0][0]=True

while que:
    y,x,move,times = que.popleft()
    if y == n-1 and x == m-1:
        result = move
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            if times == 1:
                if maps[ny][nx]==1 and not visited[ny][nx][0]:
                    que.append([ny,nx,move+1,0])
                    visited[ny][nx][0]=True
                elif maps[ny][nx]==0 and not visited[ny][nx][1]:
                    que.append([ny,nx,move+1,1])
                    visited[ny][nx][1]=True
            else:
                if maps[ny][nx]==0 and not visited[ny][nx][0]:
                    que.append([ny,nx,move+1,0])
                    visited[ny][nx][0]=True
print(result)