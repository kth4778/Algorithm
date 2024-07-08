from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
while True:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)
node_dict = {i:set([i]) for i in range(1,n+1)}
node_cnt = {i:float("inf") for i in range(1,n+1)}

for i in range(1,n+1):
    result = 0
    que = deque()
    que.append([i,i,0])
    while que:
        parents,node,cost = que.popleft()
        result = cost
        for w in graph[node]:
            if w not in node_dict[parents]:
                que.append([parents,w,cost+1])
                node_dict[parents].add(w)
    node_cnt[i] = result

min_num = min(node_cnt.values())
min_node = [i for i in node_cnt if node_cnt[i] == min_num]

print(min_num,len(min_node))
for i in sorted(min_node):
    print(i, end = ' ')