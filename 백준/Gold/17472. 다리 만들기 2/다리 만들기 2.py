from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
dy, dx = [1,0,0,-1], [0,1,-1,0]

# 1. 맵에 번호 부여
# 2. 섬끼리 가는 모든 길 구하기
# 3. 유니온 파인드로 최소 비용 구하기

setNumber = 1
visited = [[False for _ in range(M)] for _ in range(N)]
landCount = 0
landCoordinates = [None]

for i in range(N):
    for j in range(M):
        if not visited[i][j] and maps[i][j] == 1:
            landCoordinates.append([i,j])
            landCount += 1
            visited[i][j] = True
            maps[i][j] = setNumber
            que = deque()
            que.append([i,j])

            while que:
                y,x = que.popleft()

                for ii in range(4):
                    ny, nx = y + dy[ii], x + dx[ii]
                    if 0 <= ny < N and 0 <= nx < M:
                        if not visited[ny][nx] and maps[ny][nx] == 1:
                            visited[ny][nx] = True
                            maps[ny][nx] = setNumber
                            que.append([ny, nx])
            
            setNumber += 1

landDistance = [[float("INF")  for _ in range(landCount + 1)] for _ in range(landCount + 1)]

for i in range(1, landCount + 1):
    distance = [[[float("INF") for _ in range(4)] for _ in range(M)] for _ in range(N)]

    que = deque()
    que.append([landCoordinates[i][0], landCoordinates[i][1], 0, -1, i, 0])

    while que:
        y, x, move, direction, landNum, level = que.popleft()

        if level == 0:
            for j in range(4):
                ny, nx = y + dy[j], x + dx[j]
                if 0 <= ny < N and 0 <= nx < M:
                    if maps[ny][nx] == landNum:
                        if distance[ny][nx][j] > move:
                            distance[ny][nx][j] = move
                            que.append([ny, nx, move, j, landNum, 0])
                    else:
                        if distance[ny][nx][j] > move + 1:
                            distance[ny][nx][j] = move + 1
                            que.append([ny, nx, move + 1, j, landNum, 1])

        elif level == 1:
            ny, nx = y + dy[direction], x + dx[direction]

            if 0 <= ny < N and 0 <= nx < M:
                if maps[ny][nx] != 0:
                    if move < 2:
                        continue
                    else:
                        landDistance[landNum][maps[ny][nx]] = min(landDistance[landNum][maps[ny][nx]], move)
                
                else:
                    if distance[ny][nx][direction] > move + 1:
                        distance[ny][nx][direction] = move + 1
                        que.append([ny, nx, move + 1, direction, landNum, level])

parent = [i for i in range(landCount + 1)]
edges = []

def union(a,b):
    a,b = find(a), find(b)

    if a > b:
        parent[a] = b
    
    else:
        parent[b] = a


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

for start in range(1, landCount + 1):
    for end in range(1, landCount + 1):
        if landDistance[start][end] != float("INF"):
            edges.append([landDistance[start][end], start, end])
edges.sort()

answer = 0

for i in range(len(edges)):
    cost, start, end = edges[i]

    if find(start) != find(end):
        union(start, end)
        answer += cost

for i in range(1, landCount + 1):
    find(i)

if sum(parent) != landCount:
    print(-1)
else:
    print(answer)