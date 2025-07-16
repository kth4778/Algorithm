from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

answer = []
level = [0 for _ in range(N + 1)]
next_node = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
que = deque()

for _ in range(M):
  lst = list(map(int,input().split()))
  for i in range(1,lst[0]):
      level[lst[i + 1]] += 1
      next_node[lst[i]].append(lst[i + 1])

for i in range(1, N + 1):
    if level[i] == 0:
        que.append(i)
        visited[i] = True
        break
    
while que:
    node = que.popleft()
    answer.append(node)

    for nxt in next_node[node]:
        level[nxt] -= 1
      
    for i in range(1, N + 1):
        if not visited[i] and level[i] == 0:
            que.append(i)
            visited[i] = True


if len(answer) != N:
    print(0)
else:
    for i in answer:
        print(i)