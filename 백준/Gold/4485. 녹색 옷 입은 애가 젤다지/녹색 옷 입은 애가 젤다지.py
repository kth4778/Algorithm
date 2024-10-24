from collections import deque
import sys
input = sys.stdin.readline

p = 1
dy = [1,0,0,-1]
dx = [0,1,-1,0]

def Dijkstra():
    distance[0][0] = maps[0][0]
    que = deque()
    que.append([0,0])
    
    while que:
        curY, curX = que.popleft()
        curDistance = distance[curY][curX]

        for i in range(4):
            ny = curY + dy[i]
            nx = curX + dx[i]    
            if 0 <= ny < N and 0 <= nx < N:
                newDistance = curDistance + maps[ny][nx]
                if newDistance < distance[ny][nx]:
                    distance[ny][nx] = newDistance
                    que.append([ny,nx])

while True:
    N = int(input())
    
    if N == 0:
        sys.exit()
    
    maps = [list(map(int,input().split())) for _ in range(N)]
    distance = [[float("INF") for _ in range(N)] for _ in range(N)]
    Dijkstra()
    print(f"Problem {p}: {distance[N-1][N-1]}")
    p += 1
