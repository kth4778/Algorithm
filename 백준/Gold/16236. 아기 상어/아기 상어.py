from collections import deque
import copy

def solution(maps,iy,ix,size):  #맵 좌표 크기
    result = []
    n = len(maps)
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    que = deque()
    que.append([iy,ix,0,size])
    visited[iy][ix]=True
    while que:
        y,x,distance,size = que.popleft()
        if result and distance > result[0][2]:
            continue
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < n and 0 <= ny < n and maps[ny][nx]<=size and not visited[ny][nx]:
                if maps[ny][nx] == 0 or maps[ny][nx] == size:
                    que.append([ny,nx,distance+1,size])
                    visited[ny][nx] = True
                else:
                    result.append([ny,nx,distance+1])
                    visited[ny][nx]=True
    if not result:
        return False
    
    min_num = min([i[2] for i in result])
    result = [i for i in result if i[2]==min_num]
    result.sort(key=lambda x: (x[0],x[1]))

    return result[0]

a = int(input())
maps = [list(map(int,input().split())) for _ in range(a)]

que = deque()

for i in range(a):
    for w in range(a):
        if maps[i][w] == 9:
            maps[i][w] = 0
            que.append([i,w,0,0,2,maps])
            break
    if que:
        break
result = 0
while que:
    y,x,fish,distance,size,maps_assis = que.popleft()
    case = solution(maps_assis,y,x,size)

    if not case:
        continue

    ny,nx,new_distance = case

    maps_copy = copy.deepcopy(maps_assis)
    maps_copy[ny][nx]=0
    total_distance = distance+new_distance
    result = max(result,total_distance)

    if fish+1 == size:
        que.append([ny,nx,0,total_distance,size+1,maps_copy])
    else:
        que.append([ny,nx,fish+1,total_distance,size,maps_copy])
print(result)