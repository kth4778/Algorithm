import sys
input = sys.stdin.readline

N,M,T = map(int,input().split())
maps = [list(input().strip()) for _ in range(N)]
time_maps = [[-1 for _ in range(M)] for _ in range(N)]
dx = [1,0,0,-1]
dy = [0,1,-1,0]

# print(maps, time_maps)

for i in range(N):
    for j in range(M):
        if maps[i][j] == 'O':
            time_maps[i][j] = 3

def discount_time():
    answer = []

    for i in range(N):
        for j in range(M):
            if time_maps[i][j] > 0:
                if time_maps[i][j] == 1:
                    answer.append([i,j])
                time_maps[i][j] -= 1
    return answer

def bomb(lst):
    for y,x in lst:
        maps[y][x] = '.'
        time_maps[y][x] = -1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                maps[ny][nx] = '.'
                time_maps[ny][nx] = -1

def creat_bomb():
    for i in range(N):
        for j in range(M):
            if maps[i][j] == '.':
                maps[i][j] = 'O'
                time_maps[i][j] = 3

bomb(discount_time())
T -= 1
if T == 0:
    for i in maps:
        print(''.join(i))
    sys.exit()

while True:
    bomb(discount_time())
    creat_bomb()
    T -= 1
    if T == 0:
        break
    
    bomb(discount_time())
    T -= 1
    if T == 0:
        break

for i in maps:
    print(''.join(i))