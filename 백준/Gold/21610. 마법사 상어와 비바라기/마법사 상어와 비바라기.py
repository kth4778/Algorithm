# 1. 모든 구름이 d 방향으로 s칸 이동한다
# 2. 이동 후 구름 칸에서 물의 양이 1 증가
# 3. 구름이 사라진다
# 4. 구름이 있는칸 4개 방향의 대각선 바구니의 물 총량을 더함
# 5. 구름이 사라진 칸 제외하고 2 이상인 칸에 구름이 생기고 물의 양 2씩 감소

import sys
input = sys.stdin.readline

def solution(d,s):
    visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
    
    move_cloud = []
    new_cloud = []
    plus_cloud = {}

    for y,x in cloud:
        move_cloud.append([(y + dy[d] * s) % (N + 1), (x + dx[d] * s) % (N + 1)])
    
    for y,x in move_cloud:
        visited[y][x] = True

    for y,x in move_cloud:
        maps[y][x] += 1
    
    for y,x in move_cloud:
        for a,b in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            ny, nx = y + a, x + b
            if 0 <= ny < N + 1 and 0 <= nx < N + 1:
                if 0 < maps[ny][nx]:
                    maps[y][x] += 1

    for y in range(N + 1):
        for x in range(N + 1):
            if maps[y][x] >= 2 and not visited[y][x]:
                maps[y][x] -= 2
                new_cloud.append([y,x])
    return new_cloud

N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
answer = 0
N -= 1

dy = [None,0,-1,-1,-1,0,1,1,1]
dx = [None,-1,-1,0,1,1,1,0,-1]
cloud = [[N,0],[N,1],[N-1,0],[N-1,1]]

for _ in range(M):
    d,s = map(int,input().split())
    cloud = solution(d,s)

for i in maps:
    for j in i:
        answer += j

print(answer)