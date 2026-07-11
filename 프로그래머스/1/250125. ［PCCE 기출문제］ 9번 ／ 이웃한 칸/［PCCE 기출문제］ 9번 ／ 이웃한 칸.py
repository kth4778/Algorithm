def solution(board, h, w):
    answer = 0
    p = len(board)
    dy = [1,0,0,-1]
    dx = [0,1,-1,0]
    
    for i in range(4):
        ny = h + dy[i]
        nx = w + dx[i]
        if 0 <= ny < p and 0 <= nx < p:
            if board[ny][nx] == board[h][w]:
                answer += 1
    return answer