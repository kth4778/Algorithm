import sys
input = sys.stdin.readline

def find(x):
    if node_info[x] != x:
        node_info[x] = find(node_info[x])
    return node_info[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        node_info[a] = b
    else:
        node_info[b] = a

t = int(input())
for _ in range(t):
    n = int(input())
    nodes = list(map(int,input().split()))
    node_info = {i:i for i in range(1,n+1)}
    for i in range(n):
        a = i+1
        b = nodes[i]
        if find(a) != find(b):
            union(a,b)
    for i in range(n):
        a = i+1
        b = nodes[i]
        union(a,b)
    print(len(set(node_info.values())))