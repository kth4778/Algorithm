import sys
sys.setrecursionlimit(10 ** 5)

n,k = map(int,input().split())
rout = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for q in range(n):
            rout[i][j] = min(rout[i][j], rout[i][q] + rout[q][j])

visited = [False for _ in range(n)]
answer = float("INF")

def dfs(depth, cur, distance):
    global answer

    if depth == n:
        answer = min(answer, distance)
        return
    
    for next_node in range(n):
        if not visited[next_node]:
            visited[next_node] = True
            dfs(depth + 1, next_node, distance + rout[cur][next_node])
            visited[next_node] = False
        
visited[k] = True
dfs(1,k,0)
print(answer)