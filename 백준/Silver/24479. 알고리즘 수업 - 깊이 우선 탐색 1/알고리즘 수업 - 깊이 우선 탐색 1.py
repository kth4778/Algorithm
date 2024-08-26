import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(cur):
    global num
    visited[cur] = num
    num += 1

    for node in graph[cur]:
        if visited[node] == 0:
            dfs(node)

n,m,r = map(int,input().split())

visited = {i:0 for i in range(1,n+1)}
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
num = 1

graph = [sorted(i) for i in graph]
dfs(r)

for i in visited.values():
    print(i)