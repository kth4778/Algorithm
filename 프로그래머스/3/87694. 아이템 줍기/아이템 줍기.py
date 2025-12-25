from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    dy = [1, 0, 0, -1]
    dx = [0, 1, -1, 0]
    
    maps = [[0 for _ in range(102)] for _ in range(102)]
    visited = [[float("INF") for _ in range(102)] for _ in range(102)]
    que = deque()
    
    for sx, sy, ex, ey in rectangle:
        nsx, nsy, nex, ney = sx * 2, sy * 2, ex * 2, ey * 2
        
        for y in range(nsy, ney + 1):
            for x in range(nsx, nex + 1):
                if nsx < x < nex and nsy < y < ney:
                    maps[y][x] = -1
                elif maps[y][x] != -1:
                    maps[y][x] = 1
    
    que.append([characterY * 2, characterX * 2, 0])
    visited[characterY * 2][characterX * 2] = 0
    
    while que:
        y, x, move = que.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if maps[ny][nx] == 1 and visited[ny][nx] > move + 1:
                visited[ny][nx] = move + 1
                que.append([ny, nx, move + 1])
    
    return visited[itemY * 2][itemX * 2] // 2