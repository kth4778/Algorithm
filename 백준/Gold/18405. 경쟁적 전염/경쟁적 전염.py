from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
virus = [deque() for _ in range(K + 1)]
maps = []
dy, dx = [1,0,0,-1], [0,1,-1,0]

for i in range(N):
    m = list(map(int,input().split()))
    maps.append(m)

    for j in range(N):
        if m[j] > 0:
            virus[m[j]].append([i,j])

S,X,Y = map(int,input().split())

for _ in range(S):
    for i in range(1, K + 1):
        for _ in range(len(virus[i])):
            y,x = virus[i].popleft()

            for j in range(4):
                ny, nx = y + dy[j], x + dx[j]
                if 0 <= ny < N and 0 <= nx < N:
                    if maps[ny][nx] == 0:
                        virus[i].append([ny, nx])
                        maps[ny][nx] = i

print(maps[X - 1][Y - 1])