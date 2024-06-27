from collections import deque
while True:
    l,n,m = map(int,input().split())
    if l==0 and n == 0 and m == 0:
        exit()
    maps = [[] for _ in range(l)]
    for i in range(l):
        for j in range(n):
            maps[i].append(list(input()))
        a = input()
    dx = [1,0,0,-1,0,0]
    dy = [0,1,-1,0,0,0]
    dz = [0,0,0,0,1,-1]
    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(l)]
    que = deque()
    result = 'Trapped!'

    for i in range(l):
        for j in range(n):
            for w in range(m):
                if maps[i][j][w]=='S':
                    que.append([i,j,w,0])
                    visited[i][j][w]=True
                    break
            if que:
                break
        if que:
            break
    
    while que:
        z,y,x,move = que.popleft()
        if maps[z][y][x]=='E':
            result = f"Escaped in {move} minute(s)."
            break
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0<=nx<m and 0<=ny<n and 0<=nz<l and not visited[nz][ny][nx] and maps[nz][ny][nx]!='#':
                que.append([nz,ny,nx,move+1])
                visited[nz][ny][nx]=True
    print(result)
