from collections import deque
import sys
input = sys.stdin.readline

def bfs(a,b,group):
    que = deque()
    visited[a][b] = True
    maps[a][b] = str(group)
    que.append([a,b])
    cnt = 1

    while que:
        y,x = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 0 and not visited[ny][nx]:
                maps[ny][nx] = str(group)
                visited[ny][nx] = True
                que.append([ny,nx])
                cnt += 1

    graph[group] = cnt

n,m = map(int,input().split())
maps = [list(map(int,input().strip())) for _ in range(n)]
graph = {}
group = 2

dx = [1,0,0,-1]
dy = [0,1,-1,0]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0 and not visited[i][j]:
            bfs(i,j,group)
            group += 1


for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            a = set()
            for q in range(4):
                nx = j + dx[q]
                ny = i + dy[q]
                if 0 <= nx < m and 0 <= ny < n and type(maps[ny][nx]) == str:
                    a.add(maps[ny][nx])
            count = 1
            for k in a:
                count += graph[int(k)]
            maps[i][j] = count % 10

for i in range(n):
    for j in range(m):
        if type(maps[i][j]) == str:
            maps[i][j] = '0'
        elif type(maps[i][j]) == int:
            maps[i][j] = str(maps[i][j])

for i in maps:
    print(''.join(i))