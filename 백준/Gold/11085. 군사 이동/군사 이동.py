import sys
input = sys.stdin.readline

p,w = map(int,input().split())
c,v = map(int,input().split())
country = {i:i for i in range(p)}
edges = []
min_cnt = float("INF")


for _ in range(w):
    a,b,cost = map(int,input().split())
    edges.append([cost,a,b])

edges.sort(reverse=True)

def find(x):
    if x != country[x]:
        return find(country[x])
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        country[a] = b
    else:
        country[b] = a

for edge in edges:
    if find(c) == find(v):
        break
    cost,a,b = edge
    if find(a) != find(b):
        union(a,b)
        min_cnt = min(min_cnt,cost)

print(min_cnt)