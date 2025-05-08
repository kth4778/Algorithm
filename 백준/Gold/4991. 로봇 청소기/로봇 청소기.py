from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline

def minDistance(sY,sX, eY,eX):
    visited = [[float("INF") for _ in range(M)] for _ in range(N)]
    dy, dx = [1,0,0,-1], [0,1,-1,0]
    
    que = deque()
    que.append([0,sY,sX])

    while que:
        move, y, x = que.popleft()
        if y == eY and x == eX:
            return move

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if maps[ny][nx] != "x":
                    if visited[ny][nx] > move + 1:
                        visited[ny][nx] = move + 1
                        que.append([move + 1, ny, nx])

    return -1                    
                    

while True:
    M,N = map(int,input().split())
    
    if N == 0 and M == 0:
        sys.exit()


    answer = float("INF")
    maps = []
    Sy, Sx = None, None
    cleanArea = []
    
    for i in range(N):
        p = list(input().strip())
        for j in range(M):
            if p[j] == "*":
                cleanArea.append([i,j])
            elif p[j] == "o":
                Sy, Sx = i,j
        maps.append(p)

    size = len(cleanArea)
    distanceMemory = [[float("INF") for _ in range(size + 1)] for _ in range(size + 1)]
    
    for i in range(size):
        distanceMemory[0][i + 1] = minDistance(Sy, Sx, cleanArea[i][0], cleanArea[i][1])
    
    for p in permutations([i for i in range(size)], 2):
        sY, sX, eY, eX = cleanArea[p[0]][0], cleanArea[p[0]][1], cleanArea[p[1]][0], cleanArea[p[1]][1]
        distanceMemory[p[0] + 1][p[1] + 1] = minDistance(sY, sX, eY, eX)

    path = [[Sy, Sx]] + cleanArea

    for mix in permutations([i for i in range(1, size + 1)], size):
        new_path = [0] + list(mix)
        new_distance = 0

        for i in range(1, len(new_path)):
            nd = distanceMemory[new_path[i - 1]][new_path[i]]
            if nd == -1:
                new_distance = float("INF")
                break
                
            else:
                new_distance += nd

        answer = min(answer, new_distance)
    
    if answer == float("INF"):
        print(-1)
    else:
        print(answer)