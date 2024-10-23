import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(y,x):
    global sheep
    global wolf

    if maps[y][x] == "k":
        sheep += 1
    elif maps[y][x] == "v":
        wolf += 1
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            if maps[ny][nx] != "#":
                visited[ny][nx] = True
                dfs(ny, nx)

N,M = map(int,input().split())
maps = [list(input().strip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dy = [1,0,0,-1]
dx = [0,1,-1,0]
sheep_answer = 0
wolf_answer = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and maps[i][j] != "#":
            sheep = 0
            wolf = 0
            visited[i][j] = True
            dfs(i,j)
            if sheep > wolf:
                sheep_answer += sheep
            else:
                wolf_answer += wolf


print(f"{sheep_answer} {wolf_answer}")