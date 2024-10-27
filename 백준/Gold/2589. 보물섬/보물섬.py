from collections import deque
import sys
input = sys.stdin.readline

def solution(sy,sx):
    d = [[float("inf") for _ in range(M)] for _ in range(N)]
    result = 0
    d[sy][sx] = 0
    que = deque()
    que.append([sy,sx,0])

    while que:
        y,x,move = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and maps[ny][nx] == 'L':
                if d[ny][nx] > move + 1:
                    d[ny][nx] = move + 1
                    que.append([ny,nx,move + 1])

    for i in d:
        for j in i:
            if j != float("INF"):
                result = max(result, j)
    
    return result


N,M = map(int,input().split())
maps = [list(input().strip()) for _ in range(N)]
answer = 0
dy = [1,0,0,-1]
dx = [0,1,-1,0]

for i in range(N):
    for j in range(M):
        if maps[i][j] == "L":
            answer = max(answer, solution(i,j))

print(answer)