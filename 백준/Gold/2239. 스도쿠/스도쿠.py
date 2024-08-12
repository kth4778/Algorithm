board = [[int(i) for i in input()] for _ in range(9)]

def solution(board):
    def is_vaild(num, row, col):
        return not (is_row(num, row) or is_col(num, col) or is_box(num, row, col))
    
    def is_row(num, row):
        return num in board[row]
    
    def is_col(num, col):
        for i in range(9):
            if board[i][col] == num:
                return True
        return False
    
    def is_box(num, row, col):
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return True
        return False
    
    def find_position():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return [i,j]
        return None
    
    def find_soluiton():
        empty_position = find_position()

        if not empty_position:
            return True
        
        row, col = empty_position

        for num in range(1,10):
            if is_vaild(num, row, col):
                board[row][col] = num
                if find_soluiton():
                    return True
                board[row][col] = 0
        return False
    find_soluiton()
    return board

solution(board)

for i in board:
    print(''.join([str(j) for j in i]))

