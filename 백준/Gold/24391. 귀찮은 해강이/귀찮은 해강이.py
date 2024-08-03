import sys
input = sys.stdin.readline

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

n,m = map(int,input().split())
node_info = {i:i for i in range(1,n+1)}

for _ in range(m):
    a,b = map(int,input().split())
    if find(a) != find(b):
        union(a,b)

university_class = list(map(int,input().split()))
result = 0
for i in range(len(university_class)-1):
    if find(university_class[i]) != find(university_class[i+1]):
        result += 1
print(result)