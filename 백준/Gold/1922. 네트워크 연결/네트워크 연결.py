import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

edges = []
node_info = {i:i for i in range(1,n+1)}
result = 0

for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append([cost,a,b])
edges.sort()

def find_parent(node_info,x):
    if node_info[x] != x:
        node_info[x] = find_parent(node_info,node_info[x])
    return node_info[x]

def union_parent(node_info, a, b):
    a = find_parent(node_info, a)
    b = find_parent(node_info, b)
    if a < b:
        node_info[b] = a
    else:
        node_info[a] = b

for edge in edges:
    cost,a,b = edge

    if find_parent(node_info,a) != find_parent(node_info,b):
        union_parent(node_info,a,b)
        result += cost
print(result)