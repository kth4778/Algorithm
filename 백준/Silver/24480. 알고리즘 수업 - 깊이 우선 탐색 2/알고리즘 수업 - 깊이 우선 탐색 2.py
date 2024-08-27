import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def DFS(cur):
    global num
    visited[cur] = num
    num += 1
    
    for next_node in graph[cur]:
        if visited[next_node] == 0:
            DFS(next_node)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = {i:0 for i in range(1,n+1)}

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

graph = [sorted(i , reverse=True) for i in graph]
num = 1
DFS(r)

for i in visited.values():
    print(i)