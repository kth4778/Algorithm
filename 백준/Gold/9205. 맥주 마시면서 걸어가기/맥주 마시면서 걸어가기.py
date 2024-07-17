from collections import deque

result = []
t = int(input())

def bfs():
    que = deque()
    que.append(start)

    while que:
        y,x = que.popleft()
        if abs(y-end_y) + abs(x-end_x) <= 1000:
            print('happy')
            return

        for i in range(n):
            if not visited[i] and abs(y-store[i][0]) + abs(x-store[i][1]) <= 1000:
                que.append([store[i][0],store[i][1]])
                visited[i] = True
    print('sad')
    return
for _ in range(t):
    n = int(input())
    start = list(map(int,input().split()))
    store = [list(map(int,input().split())) for _ in range(n)]
    end_y,end_x = map(int,input().split())
    visited = [False for _ in range(n)]
    bfs()