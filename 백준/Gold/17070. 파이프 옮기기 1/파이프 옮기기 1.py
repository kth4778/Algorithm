import sys
input = sys.stdin.readline

def canGo(y,x,mode):
    if N <= y or N <= x:
        return False
    if maps[y][x] == 1:
        return False
    if mode == 3:
        if maps[y][x - 1] == 1 or maps[y - 1][x] == 1:
            return False
    return True

def dfs(y,x,mode):
    if y == N - 1 and x == N - 1:
        global answer
        answer += 1
        return
    
    ny, nx = y + 1, x + 1

    if canGo(ny, nx, 3):
        dfs(ny,nx,3)
    if mode != 1:
        if canGo(y + 1, x, 2):
            dfs(y + 1, x, 2)
    if mode != 2:
        if canGo(y, x + 1, 1):
            dfs(y, x + 1, 1)

N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
answer = 0
dfs(0,1,1)
print(answer)