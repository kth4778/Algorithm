import sys
input = sys.stdin.readline

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

n = int(input())
node_info = {i:i for i in range(1,n+1)}

for _ in range(n-2):
    a,b = map(int,input().split())
    if find(a) != find(b):
        union(a,b)

print(1 , end = ' ')
for i in range(2,n+1):
    if find(i) != 1:
        print(i)
        break