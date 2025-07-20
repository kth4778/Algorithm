import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]
front = [[] for _ in range(N + 1)]
cnt = [0 for _ in range(N + 1)]
time = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
total_time = [0 for _ in range(N + 1)]

for i in range(N):
    lst = list(map(int,input().split()))
    time[i + 1] = lst[0]
    total_time[i + 1] = lst[0]
    cnt[i + 1] = lst[1]
    
    for j in lst[2:]:
        graph[j].append(i + 1)
        front[i + 1].append(j)

que = deque()

for i in range(1, N + 1):
    if cnt[i] == 0:
        que.append(i)
        visited[i] = True

while que:
    n = que.popleft()

    max_num = 0

    for i in graph[n]:
        cnt[i] -= 1
    
    for i in front[n]:
        max_num = max(max_num, total_time[i])
    
    total_time[n] = time[n] + max_num

    for i in range(1, N + 1):
        if cnt[i] == 0 and not visited[i]:
            que.append(i)
            visited[i] = True

print(max(total_time))