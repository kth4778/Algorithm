from collections import deque
import sys
input = sys.stdin.readline

def distance(y1, x1, y2, x2):
    visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
    dy, dx = [1,0,0,-1], [0,1,-1,0]
    que = deque()

    que.append([y1, x1, 0])
    visited[y1][x1] = True

    while que:
        y, x, move = que.popleft()

        if y == y2 and x == x2:
            return move

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 < ny <= N and 0 < nx <= N:
                if not visited[ny][nx] and maps[ny][nx] != 1:
                    que.append([ny, nx, move + 1])
                    visited[ny][nx] = True
    return -1

def find(y, x):
    visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
    dy, dx = [1,0,0,-1], [0,1,-1,0]
    que = deque()

    que.append([y,x,0])
    visited[y][x] = True
    switch = False
    result = []

    while que:
        for _ in range(len(que)):
            gy, gx, move = que.popleft()

            if (gy, gx) in guest:
                switch = True
                result.append((gy, gx, move))

            for i in range(4):
                ny, nx = gy + dy[i], gx + dx[i]
                if 0 < ny <= N and 0 < nx <= N:
                    if maps[ny][nx] != 1 and not visited[ny][nx]:
                        que.append([ny, nx, move + 1])
                        visited[ny][nx] = True

        if switch:
            break
    
    if not result:
        return -1
    
    result.sort()
    return result[0]


N,M,oil = map(int,input().split())
maps = [[None for _ in range(N + 1)]] + [[[None]] + list(map(int,input().split())) for _ in range(N)]
startY, stratX = map(int,input().split())
guest = {}
final = {}

for i in range(M):
    y1, x1, y2, x2 = map(int,input().split())
    guest[(y1, x1)] = i + 1
    final[i + 1] = (y2, x2)

for _ in range(M):
    result = find(startY, stratX) 
    
    if result == -1 or result[2] > oil:
        print(-1)
        sys.exit()

    oil -= result[2]

    iy, ix, move1 = result[0], result[1], result[2]
    nextNum = guest[(iy, ix)]
    move2 = distance(iy, ix, final[nextNum][0], final[nextNum][1])

    if move2 == -1 or move2 > oil:
        print(-1)
        sys.exit()

    oil += move2
    startY, stratX = final[nextNum][0], final[nextNum][1]

    del guest[(iy, ix)]
    del final[nextNum]

print(oil)