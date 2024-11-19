import sys
input = sys.stdin.readline

def dfs(y, x):
    if x == M - 1:
        return True

    for i in range(3):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and maps[ny][nx] == '.':
            maps[ny][nx] = 'X'

            if dfs(ny, nx):
                return True
    return False


N,M = map(int,input().split())
maps = [list(input().strip()) for _ in range(N)]
dy = [-1,0,1]
dx = [1,1,1]

answer = 0

for i in range(N):
    if dfs(i, 0):
        answer += 1

print(answer)