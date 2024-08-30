from collections import deque

maps = [list(map(int,input().split())) for _ in range(19)]
dx = [1, 0, 1, 1] # → ↓ ↘ ↗ 
dy = [0, 1, 1, -1]

for y in range(19):
    for x in range(19):
        if maps[y][x] != 0:
            color = maps[y][x]

            for i in range(4):
                count = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and maps[ny][nx] == color:
                    count += 1

                    if count == 5:
                        if 0 <= y - dy[i] < 19 and 0 <= x - dx[i] < 19 and maps[y-dy[i]][x-dx[i]] == color:
                            break
                        if 0 <= ny + dy[i] < 19 and 0 <= nx + dx[i] < 19 and maps[ny+dy[i]][nx+dx[i]] == color:
                            break
                        print(color)
                        print(f"{y+1} {x+1}")
                        exit()

                    nx += dx[i]
                    ny += dy[i]

print(0)