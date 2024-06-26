from collections import deque

n,m = map(int,input().split())
maps = [list(input()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [1,0,0,-1]
dy = [0,1,-1,0]
fire_que = deque()
jihun_que = deque()

for i in range(n):
    for j in range(m):
        if maps[i][j]=='J':
            jihun_que.append([i,j,0])
            visited[i][j]=True
        elif maps[i][j]=='F':
            fire_que.append([i,j])

while jihun_que:
    for _ in range(len(fire_que)):
        y,x = fire_que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx]=='.':
                maps[ny][nx]='F'
                fire_que.append([ny,nx])
    for _ in range(len(jihun_que)):
        y,x,move = jihun_que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and maps[ny][nx]=='.':
                jihun_que.append([ny,nx,move+1])
                visited[ny][nx]=True
            elif nx<0 or m<=nx or ny<0 or n<=ny:
                print(move+1)
                exit()
print('IMPOSSIBLE')