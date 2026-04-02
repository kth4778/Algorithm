from collections import deque

def solution(board):
    sizeX = len(board[0])
    sizeY = len(board)
    
    visited = [[[float("inf") for _ in range(4)] for _ in range(sizeX)] for _ in range(sizeY)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우
    que = deque()
    
    Gy, Gx = -1, -1
    
    for y in range(sizeY):
        for x in range(sizeX):
            if board[y][x] == "R":
                que.append([y, x, 0])
            elif board[y][x] == "G":
                Gy, Gx = y, x
    while que:
        y, x, move = que.popleft()
        
        for i in range(4):
            ny, nx = y, x
            while True:
                if 0 <= ny + dy[i] < sizeY and 0 <=  nx + dx[i] < sizeX:
                    if board[ny + dy[i]][nx + dx[i]] != 'D':
                        ny += dy[i]
                        nx += dx[i]
                    else:
                        break
                else:
                    break
            if visited[ny][nx][i] > move + 1:
                visited[ny][nx][i] = move + 1
                que.append([ny, nx, move + 1])
                           
    answer = float("INF")
    
    for i in visited[Gy][Gx]:
        answer = min(answer, i)
    
    if answer == float("INF"):
        return -1
    return answer