from collections import deque

N = int(input())
front = [[] for _ in range(N + 1)]
back = [[] for _ in range(N + 1)]
d = [None for _ in range(N + 1)]
distance = [0 for _ in range(N + 1)]
count = [0 for _ in range(N + 1)]
visited = [False for _ in range(N  + 1)]
que = deque()

for i in range(N):
    l = list(map(int,input().split()))
    d[i + 1] = l[0]
    count[i + 1] = len(l) - 2

    for j in l[1:-1]:
        front[j].append(i + 1)
        back[i + 1].append(j)

for i in range(1, N + 1):
    if count[i] == 0:
        visited[i] = True
        que.append(i)

while que:
    m = que.popleft()
    max_distance = 0

    for i in back[m]:
        if distance[i] != 0:
            max_distance = max(max_distance, distance[i])

    for i in front[m]:
        count[i] -= 1
    
    for i in range(1, N + 1):
        if count[i] == 0 and not visited[i]:
            que.append(i)
            visited[i] = True
            break

    distance[m] = d[m] + max_distance

for i in range(1, N + 1):
    print(distance[i])