import sys
input = sys.stdin.readline

n,m = map(int,input().split())
node_info = {i:i for i in range(n)}
node_lst = [list(map(int,input().split())) for _ in range(m)]

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
    
for i in range(m):
    a,b = node_lst[i]
    if find(a) == find(b):
        print(i+1)
        sys.exit()
    union(a,b)
print(0)