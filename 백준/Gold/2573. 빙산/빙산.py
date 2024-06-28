from collections import deque
n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dx = [1,0,0,-1]
dy = [0,1,-1,0]


def solution(maps):
    ice_breg = {}
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]!=0:
                ice_breg[(i,j)]=False
    result = 0

    while True:
        if all(ice_breg.values()):
            break
        que = deque()
        for i in ice_breg:
            if not ice_breg[i]:
                que.append(i)
                ice_breg[i]=True
                break
        while que:
            y,x = que.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<len(maps[0]) and 0<=ny<len(maps) and maps[ny][nx] != 0 and not ice_breg[(ny,nx)]:
                    ice_breg[(ny,nx)]=True
                    que.append([ny,nx])
        result += 1
    return result

days = 0
k = 0
while True:
    t = solution(maps)
    if t >= 2:
        days = k
        break
    elif t == 0:
        break
        
    set_icebreg = []    
    for y in range(n):
        for x in range(m):
            if maps[y][x]!=0:
                cnt = 0
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0<=nx<m and 0<=ny<n and maps[ny][nx]==0:
                        cnt+=1
                set_icebreg.append([y,x,cnt])
    for y,x,cnt in set_icebreg:
        p = maps[y][x]-cnt
        if p<0:
            maps[y][x]=0
        else:
            maps[y][x]=p
    k += 1
print(days)