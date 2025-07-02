import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
dp = [[0,0] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(N - 1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(num):
    visited[num] = True

    dp[num][0] = 0
    dp[num][1] = 1

    for nxt in graph[num]:
        if not visited[nxt]:
            dfs(nxt)
            dp[num][0] += dp[nxt][1]
            dp[num][1] += min(dp[nxt][0], dp[nxt][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))