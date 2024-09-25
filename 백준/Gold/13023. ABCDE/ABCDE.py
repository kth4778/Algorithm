n,m = map(int,input().split())

def dfs(depth, visited, cur):
    global answer
    if depth == 4:
        answer = 1
        return
    
    visited[cur] = True
    for next_node in graph[cur]:
        if not visited[next_node]:
            dfs(depth + 1, visited, next_node)
    
    visited[cur] = False

graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    answer = 0
    dfs(0, [False] * n, i)
    if answer == 1:
        print(1)
        break
else:
    print(0)