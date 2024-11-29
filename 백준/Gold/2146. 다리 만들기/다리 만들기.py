from collections import deque
import sys
input = sys.stdin.readline

def bfs1(i,j,num):
    visited[i][j] = True
    maps[i][j] = num
    que = deque()
    que.append([i,j])

    while que:
        y,x = que.popleft()

        for q in range(4):
            ny,nx = y + dy[q], x + dx[q]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    visited[ny][nx] = True
                    maps[ny][nx] = num
                    que.append([ny,nx])

def bfs2(v):
    que = deque()
    dist = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] == v:
                dist[i][j] = 0
                que.append([i,j])
        
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny,nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if maps[ny][nx] and maps[ny][nx] != v:
                    return dist[y][x]
                
                elif not maps[ny][nx] and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    que.append([ny,nx])
    
    return float("INF")


n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dy = [1,0,0,-1]
dx = [0,1,-1,0]
num = 1
result = float("INF")

for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == 1:
            bfs1(i,j,num)
            num += 1

for i in range(1, num):
    result = min(result, bfs2(i))

print(result)