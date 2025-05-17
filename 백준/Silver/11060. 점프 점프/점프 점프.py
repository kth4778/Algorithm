from collections import deque

N = int(input())
A = list(map(int,input().split()))
distance = [float("inf") for _ in range(N)]
distance[0] = 0

que = deque()
que.append([0,0])

while que:
    cur, move = que.popleft()

    for i in range(1, A[cur] + 1):
        next_node = cur + i
        if 0 <= next_node < N:
            if distance[next_node] > move + 1:
                distance[next_node] = move + 1
                que.append([next_node, move + 1])

if distance[N - 1] == float("INF"):
    print(-1)
else:
    print(distance[N - 1])