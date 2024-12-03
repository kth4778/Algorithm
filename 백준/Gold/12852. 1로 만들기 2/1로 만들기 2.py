from collections import deque

n = int(input())
distance = [float("INF") for _ in range(n + 1)]

que = deque()
que.append([n,0,[n]])
distance[n] = 0

while que:
    cur, count, lst = que.popleft()

    if cur == 1:
        print(count)
        print(*lst)
        break

    if cur % 3 == 0 and cur // 3 > 0:
        if distance[cur // 3] > count + 1:
            distance[cur // 3] = count + 1
            que.append([cur // 3, count + 1, lst + [cur // 3]])
    
    if cur % 2 == 0 and cur // 2 > 0:
        if distance[cur // 2] > count + 1:
            distance[cur // 2] = count + 1
            que.append([cur // 2, count + 1, lst + [cur // 2]])
    
    if cur - 1 > 0:
        if distance[cur - 1] > count + 1:
            distance[cur - 1] = count + 1
            que.append([cur - 1, count + 1, lst + [cur - 1]])