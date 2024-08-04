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

n,m,k = map(int,input().split())
friends = list(map(int,input().split()))
node_info = {i:i for i in range(1,n+1)}
node_cost = {i+1:friends[i] for i in range(n)}

for _ in range(m):
    a,b = map(int,input().split())
    if find(a) != find(b):
        union(a,b)

result = 0
result = [float("INF") for _ in range(n+1)]

for i in range(1,n+1):
    root = find(i)
    result[root] = min(result[root],friends[i-1])

answers = 0

for i in range(n+1):
    if result[i] != float("INF"):
        answers += result[i]
if k < answers:
    print("Oh no")
else:
    print(answers)