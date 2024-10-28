from collections import deque
import sys
input = sys.stdin.readline

def dfs(s,e):
    visited = [False for _ in range(N + 1)]
    visited[s] = True
    
    que = deque()
    que.append([s,0])
    
    while que:
        cur, move = que.popleft()
        
        if cur == e:
            return move
        
        for next_node, distance in node_info[cur]:
            if not visited[next_node]:
                new_distance = move + distance
                visited[next_node] = True
                que.append([next_node, new_distance])


N,M = map(int,input().split())
node_info = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a,b,d = map(int,input().split())
    node_info[a].append([b,d])
    node_info[b].append([a,d])

for _ in range(M):
    s,e = map(int,input().split())
    print(dfs(s,e))