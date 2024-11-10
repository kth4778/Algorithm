from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
node = {i:0 for i in range(1, N + 1)}
node_info = [[] for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int,input().split())
    node_info[a].append(b)
    node[b] += 1

def solution():
    que = deque()
    result = []
    
    for i in range(1, N + 1):
        if node[i] == 0:
            que.append(i)
    

    while que:
        top = que.popleft()
        result.append(top)

        for next_node in node_info[top]:
            node[next_node] -= 1
            if node[next_node] == 0:
                que.append(next_node)
    
    return ' '.join([str(i) for i in result])

print(solution())