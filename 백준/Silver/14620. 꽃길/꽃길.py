from itertools import combinations

def revisited():
    global visited
    visited = [[False for _ in range(N)] for _ in range(N)]
    return

def dfs(lst):
    cost = 0

    for y,x in lst:
        if visited[y][x]:
            revisited()
            return -1
        visited[y][x] = True
        cost += garden[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not 0 <= ny < N or not 0 <= nx < N or visited[ny][nx]:
                revisited()
                return -1
            visited[ny][nx] = True
            cost += garden[ny][nx]
    revisited()        
    return cost

N = int(input())
garden = [list(map(int,input().split())) for _ in range(N)]
min_cost = float("INF")
visited = [[False for _ in range(N)] for _ in range(N)]
dx = [1,0,0,-1]
dy = [0,1,-1,0]


for i in combinations([[i, j] for i in range(N) for j in range(N)], 3):
    p = dfs(list(i))
    if dfs(list(i)) != -1:
        min_cost = min(min_cost, p)

print(min_cost)