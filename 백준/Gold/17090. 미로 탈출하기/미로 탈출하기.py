import sys
sys.setrecursionlimit(600000)
input = sys.stdin.readline

def dfs(y,x):
    if y < 0 or y >= N or x < 0 or x >= M:
        return 1
    
    if arr[y][x] != -1:
        return arr[y][x]

    arr[y][x] = 0
    p = cache[maps[y][x]]
    arr[y][x] = max(arr[y][x], dfs(y + p[0], x + p[1]))
    return arr[y][x]

N,M = map(int,input().split())
maps = [list(input().strip()) for _ in range(N)]
arr = [[-1 for _ in range(M)] for _ in range(N)]
cache = {"R":(0,1), "L":(0,-1), "U":(-1,0), "D":(1,0)}


for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            arr[i][j] = dfs(i,j)

answer = 0

for i in arr:
    answer += sum(i)

print(answer)