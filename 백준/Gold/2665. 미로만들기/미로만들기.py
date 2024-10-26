import heapq
import sys
input = sys.stdin.readline

N = int(input())
maps = [list(input().strip()) for _ in range(N)]
visited = [[float("INF") for _ in range(N)] for _ in range(N)]
q = []
dy = [1,0,0,-1]
dx = [0,1,-1,0]

heapq.heappush(q,[0,0,0])
while q:
    cnt, y, x = heapq.heappop(q)
    if y == N - 1 and x == N - 1:
        print(cnt)
        sys.exit()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx  < N:
            if maps[ny][nx] == '0':
                if visited[ny][nx] > cnt + 1:
                    visited[ny][nx] = cnt + 1
                    heapq.heappush(q,[cnt + 1, ny, nx])
            elif maps[ny][nx] == '1':
                if visited[ny][nx] > cnt:
                    visited[ny][nx] = cnt
                    heapq.heappush(q,[cnt, ny, nx])