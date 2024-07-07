from collections import deque

def dfs(start):
    distance = [-1 for _ in range(n+1)]
    que = deque()
    que.append(start)
    distance[start] = 0
    while que:
        node = que.popleft()
        for next_node,cost in tree[node]:
            if distance[next_node] == -1:
                distance[next_node] = cost + distance[node]
                que.append(next_node)
    result = distance.index(max(distance))
    return result,distance[result]

n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

idx,_ = dfs(1)
_,result = dfs(idx)

print(result)