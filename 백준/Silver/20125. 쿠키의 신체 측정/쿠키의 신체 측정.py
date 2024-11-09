import sys
input = sys.stdin.readline

dx = [-1,1,0] #좌우하
dy = [0,0,1]

def solution(mode, y, x, bool):
    count = 0
    while 0 <= y < N and 0 <= x < N and maps[y][x] == '*':
        count += 1
        y += dy[mode]
        x += dx[mode]

    if bool:
        return y - dy[mode], x - dx[mode], count
    return count

N = int(input())
maps = [list(input().strip()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if maps[i][j] == '*':
            
            left_arm = solution(0,i + 1, j - 1, False)
            right_arm = solution(1,i + 1, j + 1, False)
            ny, nx , body = solution(2, i + 2, j, True)
            left_leg = solution(2, ny + 1, nx - 1, False)
            right_leg = solution(2, ny + 1, nx + 1, False)
            print(f"{i + 2} {j + 1}")
            print(f"{left_arm} {right_arm} {body} {left_leg} {right_leg}")
            sys.exit()