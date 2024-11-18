import sys
input = sys.stdin.readline

def solution(zongsuY,zongsuX):
    new_crazy = {}
    update_crazy = []

    for y,x in crazy:
        maps[y][x] = '.'

    for y,x in crazy:
        p = min([[y + dy[i], x + dx[i]] for i in range(1, 10) if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M], key = lambda pos : (abs(zongsuY - pos[0]) + abs(zongsuX - pos[1])))
        ny, nx = p
            
        if maps[ny][nx] == "I":
            print(f"kraj {i + 1}")
            sys.exit()

        if (ny, nx) in new_crazy:
            new_crazy[(ny, nx)] += 1
        else:
            new_crazy[(ny, nx)] = 1
        
    for (ny, nx), count in new_crazy.items():
        if count == 1:
            maps[ny][nx] = "R"
            update_crazy.append([ny, nx]) 

    return update_crazy

N,M = map(int,input().split())      #행열 입력
zongsuY, zongsuX = None, None       #종수의 좌표값
maps = []                           #보드
crazy = []                          #미친 아두이노 좌표값

for i in range(N):
    map = list(input().strip())
    maps.append(map)
    for j in range(M):
        if map[j] == "R":
            crazy.append([i,j])
        
        elif map[j] == "I":
            zongsuY, zongsuX = i,j

rout = [int(i) for i in list(input().strip())]

dx = [None,-1,0,1,-1,0,1,-1,0,1]
dy = [None,1,1,1,0,0,0,-1,-1,-1]

for i, move in enumerate(rout):
    maps[zongsuY][zongsuX] = '.'
    zongsuY,zongsuX = zongsuY + dy[move], zongsuX + dx[move]
    
    if maps[zongsuY][zongsuX] == "R":
        print(f"kraj {i + 1}")
        sys.exit()

    maps[zongsuY][zongsuX] = "I"

    next_crazy = solution(zongsuY,zongsuX)
    
    crazy = next_crazy

for i in maps:
    print(''.join(i))