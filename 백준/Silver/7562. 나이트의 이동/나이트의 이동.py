from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
t = int(input())
for _ in range(t):
    chess = int(input())
    start_x, start_y = map(int,input().split())
    end_x, end_y = map(int,input().split())
    
    que = deque()
    visited = [[False for _ in range(chess)] for _ in range(chess)]
    que.append([start_x,start_y,0])
    visited[start_x][start_y]=True
    min_move = 0
    while que:
        x,y,move = que.popleft()
        if x == end_x and y == end_y:
            min_move=move
            break
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<chess and 0<=ny<chess and not visited[nx][ny]:
                que.append([nx,ny,move+1])
                visited[nx][ny]=True
    print(min_move)
