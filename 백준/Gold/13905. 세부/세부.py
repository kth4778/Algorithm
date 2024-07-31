from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n,m = map(int,input().split())
s,e = map(int,input().split())
node_info = {i:i for i in range(1,n+1)}
edges = []
tree = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append([cost,a,b])

edges.sort(reverse = True)

def find(x):
    if x != node_info[x]:
        node_info[x] = find(node_info[x])
    return node_info[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        node_info[a] = b
    else:
        node_info[b] = a

for cost,a,b in edges:
    if find(a) != find(b):
        union(a,b)
        tree[a].append([cost,b])
        tree[b].append([cost,a])

que = deque()
que.append([s,float("INF")])
visited = [False for _ in range(n+1)]
visited[s] = True

while que:
    cur,move = que.popleft()
    if cur == e:
        print(move)
        sys.exit()
    for weight,node in tree[cur]:
        if not visited[node]:
            que.append([node,min(weight,move)])
            visited[node] = True
print(0)