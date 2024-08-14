chess = [list(map(int,input().split())) for _ in range(9)]

def solution():
    def is_vaild(num, row, col):
        return not (is_row(num, row) or is_col(num, col) or is_box(num, row, col))
    
    def is_row(num, row):
        return num in chess[row]
    
    def is_col(num, col):
        for i in range(9):
            if chess[i][col] == num:
                return True
        return False
    
    def is_box(num, row, col):
        new_row = (row // 3) * 3
        new_col = (col // 3) * 3
        for i in range(new_row, new_row + 3):
            for j in range(new_col, new_col + 3):
                if chess[i][j] == num:
                    return True
        return False
    
    def find_zero():
        for i in range(9):
            for j in range(9):
                if chess[i][j] == 0:
                    return [i,j]
        return None
    
    def find_solution():
        empty_position = find_zero()
        if not empty_position:
            return True
        
        row, col = empty_position
        for num in range(1,10):
            if is_vaild(num, row, col):
                chess[row][col] = num
                if find_solution():
                    return True
                chess[row][col] = 0
        return False
    
    find_solution()
    return chess

solution()
for i in chess:
    print(*i)