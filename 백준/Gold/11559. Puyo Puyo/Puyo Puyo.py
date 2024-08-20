from collections import deque

def removePPu(i,j,s):
    visited = [[False for _ in range(6)] for _ in range(12)]
    que = deque()
    que.append([i,j])
    visited[i][j] = True
    lst = [[i,j]]

    while que:
        y,x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < 6 and 0 <= ny < 12 and not visited[ny][nx]:
                if maps[ny][nx] == s:
                    lst.append([ny,nx])
                    visited[ny][nx] = True
                    que.append([ny,nx])
    if len(lst) >= 4:
        for q,w in lst:
            maps[q][w] = '.'
        return True

def bfs():
    answer = 0
    
    while True:
        switch = False
        for i in range(12):
            for j in range(6):
                if maps[i][j] != '.':
                    if removePPu(i,j,maps[i][j]):
                        switch = True
        
        if not switch:
            break

        answer += 1

    if answer == 0:
        return False
    return True

def change_maps():
    for x in range(6):
        stack = []
        for y in range(12):
            if maps[y][x] != '.':
                stack.append(maps[y][x])

        for i in reversed(range(12)):
            if stack:
                maps[i][x] = stack.pop()
            else:
                maps[i][x] = '.' 
            

maps = [list(input()) for _ in range(12)]
dy = [1,0,0,-1]
dx = [0,1,-1,0]
answer = 0

while True:
    if bfs():
        answer += 1
        change_maps()
    else:
        break
print(answer)