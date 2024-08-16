from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j,k):
    que = deque()
    que.append([i,j])
    while que:
        y,x = que.popleft()
        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and maps[ny][nx] > k:
                visited[ny][nx] = True
                que.append([ny,nx])

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
dx = [1,0,0,-1]
dy = [0,1,-1,0]

max_rain = 0
result = 0

for i in range(n):
    for j in range(n):
        max_rain = max(max_rain, maps[i][j])

for k in range(max_rain):
    visited = [[False for _ in range(n)] for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(n):
            if maps[i][j] > k and not visited[i][j]:
                visited[i][j] = True
                bfs(i,j,k)
                answer += 1

    result = max(result, answer)

print(result)
