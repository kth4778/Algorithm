import sys
input = sys.stdin.readline

n = int(input())
node_count = [1 for _ in range(1000001)]
node_info = [i for i in range(1000001)]

def find(x):
    if node_info[x] != x:
        node_info[x] = find(node_info[x])
    return node_info[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        node_info[b] = a
        node_count[a] += node_count[b]
    else:
        node_info[a] = b
        node_count[b] += node_count[a]

for _ in range(n):
    l = list(input().split())
    if l[0] == 'I':
        a = int(l[1])
        b = int(l[2])
        if find(a) != find(b):
            union(a,b)
    else:
        x = int(l[1])
        print(node_count[find(x)])