def solution(board, moves):
    length = len(board)
    result = 0
    lst = []
    visited = [[False for _ in range(length)] for _ in range(length)]
    
    for m in moves:
        for i in range(length):
            if not visited[i][m - 1] and board[i][m - 1] != 0:
                visited[i][m - 1] = True
                if lst and lst[-1] == board[i][m - 1]:
                    lst.pop()
                    result += 2
                else:
                    lst.append(board[i][m - 1])
                break
    return result