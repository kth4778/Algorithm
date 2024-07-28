from collections import deque

s = int(input())
visited = [[False for _ in range(1001)] for _ in range(1001)]
distance = [[float("INF") for _ in range(1001)] for _ in range(1001)]
que = deque()
que.append([1,0])
distance[1][0] = 0
visited[1][0] = True

while que:
    screen,clip = que.popleft()
    if screen == s:
        print(distance[screen][clip])
        break
    for a,b in [[screen,screen],[screen+clip,clip],[screen-1,clip]]:
        if 0 <= a <= 1000 and not visited[a][b]:
            if distance[a][b] > distance[screen][clip] + 1:
                distance[a][b] = distance[screen][clip] + 1
                visited[a][b] = True
                que.append([a,b])