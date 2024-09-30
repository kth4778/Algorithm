N, M, A, B, C = map(int,input().split())

def dfs(visited, cur, money, max_cost):
    if cur == B:
        global answer
        answer = min(max_cost, answer)
        return

    visited[cur] = True
    for next_node, cost in node_info[cur]:
        if not visited[next_node] and money - cost >= 0:
            dfs(visited, next_node, money - cost, max(cost, max_cost))
            visited[next_node] = False



node_info = [[] for _ in range(N + 1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    node_info[a].append([b,c])
    node_info[b].append([a,c])

answer = float("INF")
dfs([False] * (N + 1), A, C, -1)
if answer == float("INF"):
    print(-1)
else:
    print(answer)