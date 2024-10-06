import sys
input = sys.stdin.readline

def dfs(t, n, size):
    global answer
    size += snow[n]

    if t == M:
        answer = max(answer, size)
        return
    if n == N - 1:
        answer = max(answer, size)
        return
    
    n1, n2 = n + 1, n + 2
    if n1 < N:
        dfs(t + 1, n1, size)
    if n2 < N:
        dfs(t + 1, n2, size // 2)

N,M = map(int,input().split())
snow = list(map(int,input().split()))
answer = 0
dfs(1, 0, 1)
if N > 1:
    dfs(1,1,0)
print(answer)
