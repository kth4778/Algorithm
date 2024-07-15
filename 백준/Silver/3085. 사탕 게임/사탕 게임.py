n = int(input())
board = [list(input()) for _ in range(n)]

def solution(board):
    lst = []
    set_alpha = None
    for i in range(n):
        lst.append(1)
        set_alpha = board[i][0]
        for w in range(1,n):
            if board[i][w] == set_alpha:
                lst[-1] += 1
            elif board[i][w] != set_alpha:
                lst.append(1)
                set_alpha = board[i][w]

    for i in range(n):
        lst.append(1)
        set_alpha = board[0][i]
        for w in range(1,n):
            if board[w][i] == set_alpha:
                lst[-1] += 1
            elif board[w][i] != set_alpha:
                lst.append(1)
                set_alpha = board[w][i]
    return max(lst)

max_size = 0
dx = [0,1]
dy = [1,0]

for y in range(n):
    for x in range(n):
        for w in range(2):
            nx = x+dx[w]
            ny = y+dy[w]
            if nx < n and ny < n and board[y][x] != board[ny][nx]:
                board[y][x],board[ny][nx] = board[ny][nx],board[y][x]
                max_size = max(max_size,solution(board))
                board[ny][nx],board[y][x] = board[y][x],board[ny][nx]
            
print(max_size)