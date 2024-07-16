from collections import deque
import sys
input = sys.stdin.readline

def dust(maps):
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    dust_lst = []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] > 0:
                dust_lst.append([i,j])
    second_dust = []

    for y,x in dust_lst:
        cnt = 0
        amount = maps[y][x]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != -1:
                second_dust.append([ny,nx,amount//5])
                cnt += 1
        maps[y][x] -= amount//5 * cnt

    for y,x,w in second_dust:
        maps[y][x] += w   

def cleaning(maps):
    coordinate1 = None
    coordinate2 = None

    dx = [1,0,-1,0] #우상좌하
    dy = [0,-1,0,1]
    
    for i in range(n):
        if maps[i][0] == -1:
            coordinate1,coordinate2 = i,i+1
            break
    que1 = deque()
    que1.append([coordinate1,0,0])
    idx = 0
    while que1:
        y,x,amount = que1.popleft()
        if idx != 0 and y == coordinate1 and x == 0:
            break

        ny,nx = dy[idx]+y ,dx[idx]+x
        if 0 <= nx < m and 0 <= ny < n:
            que1.append([ny,nx,maps[ny][nx]])
            maps[ny][nx] = amount
        else:
            idx += 1
            que1.append([y,x,amount])
    maps[coordinate1][0] = -1

    que2 = deque()
    que2.append([coordinate2,0,0])
    idx = 0
    while que2:
        y,x,amount = que2.popleft()
        if idx != 0 and y == coordinate1 and x == 0:
            break

        ny,nx = dy[idx]+y ,dx[idx]+x
        if 0 <= nx < m and 0 <= ny < n:
            que2.append([ny,nx,maps[ny][nx]])
            maps[ny][nx] = amount
        else:
            idx -= 1
            que2.append([y,x,amount])
    maps[coordinate2][0] = -1
        
    
n,m,t = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

for _ in range(t):
    dust(maps)
    cleaning(maps)

result = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] != -1:
            result += maps[i][j]
print(result)