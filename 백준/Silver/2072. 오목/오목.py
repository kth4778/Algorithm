from collections import deque
import sys
input = sys.stdin.readline

def isTrue(color, y, x):
    count = [1,1,1,1]
    que1 = deque()
    que2 = deque()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 19 and 0 <= ny < 19:
            if boards[ny][nx] == color:
                que1.append([ny,nx,i])
                count[i] += 1
    
    while que1:
        q,w,direction = que1.popleft()
        nq = q + dy[direction]
        nw = w + dx[direction]
        if 0 <= nw < 19 and 0 <= nq < 19:
            if boards[nq][nw] == color:
                que1.append([nq,nw,direction])
                count[direction] += 1

    for i in range(4):
        nx = x - dx[i]
        ny = y - dy[i]
        if 0 <= nx < 19 and 0 <= ny < 19:
            if boards[ny][nx] == color:
                que2.append([ny,nx,i])
                count[i] += 1
    
    while que2:
        q,w,direction = que2.popleft()
        nq = q - dy[direction]
        nw = w - dx[direction]
        if 0 <= nw < 19 and 0 <= nq < 19:
            if boards[nq][nw] == color:
                que2.append([nq,nw,direction])
                count[direction] += 1
    for i in count:
        if i == 5:
            return True
    return False

    

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
boards = [[0 for _ in range(19)] for _ in range(19)] # 1: 흰, 2: 검
dx = [1,0,1,1]
dy = [0,1,1,-1]

for i in range(n):
    y,x = lst[i]
    y -= 1
    x -= 1
    if i % 2 == 0:
        boards[y][x] = 1
    else:
        boards[y][x] = 2
    if isTrue(boards[y][x], y, x):
        print(i + 1)
        exit()
print(-1)