import sys
input = sys.stdin.readline

t = int(input())
cnt = 1

def find(x):
    if x != node_info[x]:
        node_info[x] = find(node_info[x])
    return node_info[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        node_info[b] = a
    else:
        node_info[a] = b

for i in range(t):
    print(f"Scenario {i+1}:")
    n = int(input())
    k = int(input())

    node_info = {i:i for i in range(n)}
    for _ in range(k):
        a,b = map(int,input().split())
        if find(a) != find(b):
            union(a,b)

    m = int(input()) 
    for _ in range(m):
        u,v = map(int,input().split())
        if find(u) != find(v):
            print(0)
        else:
            print(1)
    if cnt == t:
        continue
    cnt += 1
    print()