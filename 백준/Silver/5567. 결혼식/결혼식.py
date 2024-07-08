n = int(input())
m = int(input())
lst = [list(map(int,input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
for a,b in lst:
    graph[a].append(b)
    graph[b].append(a)
result = set()

for i in graph[1]:
    result.add(i)
    for w in graph[i]:
        result.add(w)
if len(result) == 0:
    print(0)
else:
    print(len(result)-1)
