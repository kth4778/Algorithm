import copy

N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
cctv = []
result = float("INF")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cctv_modes = [
    [],
    [[0], [1], [2], [3]],                # 1번: 한쪽
    [[0, 2], [1, 3]],                    # 2번: 직선(좌우/상하)
    [[0, 1], [1, 2], [2, 3], [3, 0]],    # 3번: 직각(L자)
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], # 4번: 3방향(T자)
    [[0, 1, 2, 3]]                       # 5번: 4방향
]

for y in range(N):
    for x in range(M):
        if 0 < maps[y][x] < 6:
            cctv.append([maps[y][x], y, x])

def find_result(copy_maps, index):
    if index == len(cctv):
        global result
        count = 0

        for i in range(N):
            for j in range(M):
                if copy_maps[i][j] == 0:
                    count += 1
        result = min(result, count)
        return

    direction, y, x = cctv[index]

    for i in cctv_modes[direction]:
        p = copy.deepcopy(copy_maps)
        for j in i:
            ny, nx = y, x
            while True:
                ny, nx = ny + dy[j], nx + dx[j]
                if 0 <= ny < N and 0 <= nx < M and p[ny][nx] != 6:
                    p[ny][nx] = -1
                else:
                    break
        find_result(p, index + 1)

find_result(maps, 0)
print(result)