from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    maps = [list(input().rstrip()) for _ in range(n)]
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    fire_que = deque()
    sang_que = deque()
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j]=='@':
                sang_que.append([i,j,1])
                visited[i][j]=True
            elif maps[i][j]=='*':
                fire_que.append([i,j])
    
    min_move = 'IMPOSSIBLE'
    switch = False

    while sang_que:
        for _ in range(len(fire_que)):
            y,x = fire_que.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<m and 0<=ny<n and maps[ny][nx]=='.':
                    maps[ny][nx]='*'
                    fire_que.append([ny,nx])
        
        for _ in range(len(sang_que)):
            y,x,move = sang_que.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<m and 0<=ny<n:
                    if maps[ny][nx]=='.' and not visited[ny][nx]:
                        sang_que.append([ny,nx,move+1])
                        visited[ny][nx]=True
                else:
                    min_move = move
                    switch = True
                    break
            if switch:
                break
        if switch:
            break
    print(min_move)