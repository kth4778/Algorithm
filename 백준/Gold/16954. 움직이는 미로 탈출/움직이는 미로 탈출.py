from collections import deque

def solution():
    global visited
    que = deque()
    que.append([7,0])

    while que:
        for _ in range(len(que)):
            y,x = que.popleft()

            for i in range(9):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < 8 and 0 <= nx < 8:
                    if not visited[ny][nx] and maps[ny][nx] == '.':
                        if ny == 0 and nx == 7:
                            return 1
                        visited[ny][nx] = True
                        que.append([ny,nx])


        for i in range(7,0,-1):
            maps[i] = maps[i - 1]
        maps[0] = ['.' for _ in range(8)]
        
        for _ in range(len(que)):
            y,x = que.popleft()
            if maps[y][x] == '.':
                que.append([y,x])
        visited = [[False for _ in range(8)] for _ in range(8)]
    
    return 0



maps = [list(input()) for _ in range(8)]
visited = [[False for _ in range(8)] for _ in range(8)]
dy = [1,0,0,-1,0,1,1,-1,-1]
dx = [0,1,-1,0,0,1,-1,1,-1]

print(solution())