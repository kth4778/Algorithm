from collections import deque
import copy
import sys
input = sys.stdin.readline

def solution():
    empty_que = deque()
    empty_que.append([0,0])
    empty[0][0] = True

    while empty_que:
        y,x = empty_que.popleft()
    
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if maps[ny][nx] == 0 and not empty[ny][nx]:
                    empty[ny][nx] = True
                    empty_que.append([ny,nx])

cheeze = deque()
N,M = map(int,input().split())
copy_empty = [[False for _ in range(M)] for _ in range(N)] 
empty = None
maps = []
time = 0
dy = [1,0,0,-1]
dx = [0,1,-1,0]

for i in range(N):
    m = list(map(int,input().split()))
    maps.append(m)
    for j in range(M):
        if m[j] == 1:
            cheeze.append([i,j])

test = 0
while cheeze:
    empty = copy.deepcopy(copy_empty)
    solution()
    time += 1
    delete_cheeze = []

    for _ in range(len(cheeze)):
        y,x = cheeze.popleft()
        cnt = 0
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if maps[ny][nx] == 0 and empty[ny][nx]:
                    cnt += 1
        
        if cnt >= 2:
           delete_cheeze.append([y,x])
        else:
            cheeze.append([y,x])

    for y, x in delete_cheeze:
        maps[y][x] = 0

        
    
print(time)