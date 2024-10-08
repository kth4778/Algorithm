import sys
input = sys.stdin.readline

def dfs(n, c):
    global answer
    
    if c + (L - n + 1) // 2 <= answer:
        return
    if n >= L:
        answer = max(answer, c)
        return

    for y,x in lst[n]:
        if not v[y - x + N]:
            v[y - x + N] = True
            dfs(n + 2, c + 1)
            v[y - x + N] = False
    dfs(n + 2, c)

N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
L = 2 * N - 1
lst = [[] for _ in range(L)]
v = [False] * (L + 1)
answer = 0

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            lst[i + j].append([i,j])

dfs(0, 0)
t = answer
answer = 0
dfs(1,0)
print(answer + t)