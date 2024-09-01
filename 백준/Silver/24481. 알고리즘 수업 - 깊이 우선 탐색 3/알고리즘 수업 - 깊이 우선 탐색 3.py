import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node):
    graph[node].sort()
    for next_node in graph[node]:
        if visited[next_node] == -1:
            visited[next_node] = visited[node] + 1
            dfs(next_node)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[r] = 0
dfs(r)

for i in visited[1:]:
    print(i)