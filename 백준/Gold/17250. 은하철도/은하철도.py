import sys
input = sys.stdin.readline

n,m = map(int,input().split())
galaxy = {}
node_info = {i:i for i in range(1,n+1)}
for i in range(n):
    galaxy[i+1] = int(input())

def find(x):
    if x != node_info[x]:
        node_info[x] = find(node_info[x])
    return node_info[x]

def union(a,b):
    if a < b:
        galaxy[a] += galaxy[b]
        node_info[b] = a
        return galaxy[a]
    else:
        galaxy[b] += galaxy[a]
        node_info[a] = b
        return galaxy[b]
    

for _ in range(m):
    a,b = map(int,input().split())
    a = find(a)
    b = find(b)
    if a == b:
        print(galaxy[a])
    else:
        print(union(a,b))