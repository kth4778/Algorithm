from collections import deque

n,m = map(int,input().split())
maps = [list(input()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for w in range(m):
        if maps[i][w]=='#':
            visited[i][w]=True
sheep = 0
wolf = 0
result = [0,0]

dx = [1,0,0,-1]
dy = [0,1,-1,0]

def solution(lst):
    for i in lst:
        for w in i:
            if not w:
                return True
    return False

while solution(visited):
    que = deque()
    switch = False
    for i in range(n):
        for w in range(m):
            if visited[i][w]==False:
                que.append([i,w])
                visited[i][w]=True
                if maps[i][w]=='o':
                    sheep+=1
                elif maps[i][w]=='v':
                    wolf+=1
                break
        if que:
            break
    while que:

        y,x = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and maps[ny][nx] !='#':
                if maps[ny][nx]=='o':
                    sheep+=1
                    que.append([ny,nx])
                    visited[ny][nx]=True
                elif maps[ny][nx]=='v':
                    wolf+=1
                    que.append([ny,nx])
                    visited[ny][nx]=True
                else:
                    que.append([ny,nx])
                    visited[ny][nx]=True
    if sheep<=wolf:
        result[1]+=wolf
    else:
        result[0]+=sheep
    wolf = 0
    sheep = 0

print(' '.join([str(i) for i in result]))
