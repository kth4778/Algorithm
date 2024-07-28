from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
maps = [list(input().strip()) for _ in range(n)]

dx = [1,0,0,-1]
dy = [0,1,-1,0]
visited = [[False for _ in range(m)] for _ in range(n)]

def W(y,x):
    answers = 1
    visited[y][x] = True
    que = deque()
    que.append([y,x])

    while que:
        a,b = que.popleft()
        for i in range(4):
            nx = b + dx[i]
            ny = a + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maps[ny][nx] == 'W':
                answers += 1
                que.append([ny,nx])
                visited[ny][nx] = True
    return answers ** 2

def B(y,x):
    answers = 1
    visited[y][x] = True
    que = deque()
    que.append([y,x])
    while que:
        a,b = que.popleft()
        for i in range(4):
            nx = b + dx[i]
            ny = a + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and maps[ny][nx] == 'B':
                answers += 1
                que.append([ny,nx])
                visited[ny][nx] = True
    return answers ** 2

white_power = 0
blue_power = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if maps[i][j] == 'W':
                white_power += W(i,j)
            else:
                blue_power += B(i,j)

print(white_power,end = ' ')
print(blue_power)