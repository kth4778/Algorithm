from collections import deque
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
maps = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    y,x = map(int,input().split())
    maps[y-1][x-1] = 1

dx = [1,0,0,-1]
dy = [0,1,-1,0]
visited = [[False for _ in range(m)] for _ in range(n)]

max_area = 0
def bfs(a,b):
    que = deque()
    visited[a][b] = True
    answers = 1
    que.append([a,b])

    while que:
        y,x = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maps[ny][nx] == 1:
                visited[ny][nx] = True
                answers += 1
                que.append([ny,nx])
    return answers

for i in range(n):
    for j in range(m):
        if not visited[i][j] and maps[i][j] == 1:
            max_area = max(max_area,bfs(i,j))
print(max_area)