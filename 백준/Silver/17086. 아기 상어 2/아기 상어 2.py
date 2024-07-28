from collections import deque

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
max_move = 0

def bfs(a,b):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[a][b] = True
    que = deque()
    que.append([a,b,0])
    dx = [1,0,0,-1,1,1,-1,-1]
    dy = [0,1,-1,0,1,-1,1,-1]

    while que:
        y,x,move = que.popleft()
        if maps[y][x] == 1:
            return move
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                visited[ny][nx] = True
                que.append([ny,nx,move+1])

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            max_move = max(max_move,bfs(i,j))
print(max_move)