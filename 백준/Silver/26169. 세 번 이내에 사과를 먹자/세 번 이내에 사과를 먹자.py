def dfs(cnt, move, y, x):
    p = maps[y][x]

    if move > 3:
        return
    if p == 1:
        cnt += 1
    if cnt >= 2:
        global answer
        answer = 1
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if maps[ny][nx] != -1:
                maps[y][x] = -1
                dfs(cnt, move + 1, ny, nx)
                maps[y][x] = p




maps = [list(map(int,input().split())) for _ in range(5)]
n,m = map(int,input().split())
dx = [1,0,0,-1]
dy = [0,1,-1,0]


answer = 0
dfs(0, 0, n, m)
print(answer)