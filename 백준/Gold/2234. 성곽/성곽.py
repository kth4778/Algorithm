import sys
input = sys.stdin.readline
from collections import deque

def change(num):
    answer = ""
    while num > 0:
        answer += str(num % 2)
        num //= 2
    return (answer[::-1]).zfill(4)

def bfs(No,y,x):
    lst = [[y,x]]
    que = deque()
    num = 1
    que.append([y,x])
    visited[y][x] = True
    
    while que:
        y,x = que.popleft()
        for i in range(4):
            if maps[y][x][i] == '1':
                continue
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                num += 1
                lst.append([ny,nx])
                que.append([ny,nx])
                visited[ny][nx] = True
    
    for q,w in lst:
        maps[q][w] = [No,num]

def bfs2(y,x):
    global Max_num
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and maps[y][x][0] != maps[ny][nx][0]:
            Max_num = max(Max_num, maps[y][x][1] + maps[ny][nx][1])

m,n = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
maps = [[change(j) for j in i]for i in maps]   #남동북서
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
No = 0
Max_num = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(No,i,j)
            No += 1

for i in range(n):
    for j in range(m):
        bfs2(i,j)

print(No)
print(max([j[1] for i in maps for j in i]))
print(Max_num)