import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(y, x):
    if arr[y][x]:
        return arr[y][x]
    
    arr[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < N:
            if maps[ny][nx] > maps[y][x]:
                arr[y][x] = max(arr[y][x], dfs(ny,nx) + 1)
        
    return arr[y][x]

N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
arr = [[0 for _ in range(N)] for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

answer = 0
for i in range(N):
    for j in range(N):
        if not arr[i][j]:
            dfs(i,j)

for i in arr:
    answer = max(answer, max(i))

print(answer)