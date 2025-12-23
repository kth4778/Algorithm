import heapq

def solution(land, height):
    size = len(land)
    visited = [[False for _ in range(size)] for _ in range(size)]

    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    que = []
    total_cost = 0
    heapq.heappush(que, [0,0,0])

    while que:
        cost, y, x = heapq.heappop(que)

        if visited[y][x]:
            continue

        visited[y][x] = True
        total_cost += cost

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < size and 0 <= nx < size:
                if not visited[ny][nx]:
                    if abs(land[y][x] - land[ny][nx]) > height:
                        heapq.heappush(que, [abs(land[y][x] - land[ny][nx]), ny, nx])
                    else:
                        heapq.heappush(que, [0, ny, nx])
    return total_cost