n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
result=[]
def Tetromino_rectangle_1(lst):
    for i in range(n):
        for w in range(m-3):
            result.append(sum(lst[i][w:w+4]))
def Tetromino_rectangle_2(lst):
    for i in range(n-3):
        for w in range(m):
            result.append(sum([lst[i][w],lst[i+1][w],lst[i+2][w],lst[i+3][w]]))
def Tetromino_square(lst):
    for i in range(n-1):
        for w in range(m-1):
            result.append(sum([lst[i][w],lst[i][w+1],lst[i+1][w],lst[i+1][w+1]]))
def Tetromino_L1(lst):
    for i in range(n-2):
        for w in range(m-1):
            result.append(sum([lst[i][w],lst[i+1][w],lst[i+2][w],lst[i+2][w+1]]))
def Tetromino_L2(lst):
    for i in range(n-2):
        for w in range(1,m):
            result.append(sum([lst[i][w],lst[i+1][w],lst[i+2][w],lst[i+2][w-1]]))
def Tetromino_L3(lst):
    for i in range(n-2):
        for w in range(m-1):
            result.append(sum([lst[i][w],lst[i+1][w],lst[i+2][w],lst[i][w+1]]))
def Tetromino_L4(lst):
    for i in range(n-2):
        for w in range(1,m):
            result.append(sum([lst[i][w],lst[i+1][w],lst[i+2][w],lst[i][w-1]]))
def Tetromino_L5(lst):
    for i in range(n-1):
        for w in range(m-2):
            result.append(sum([lst[i][w+2],lst[i+1][w],lst[i+1][w+1],lst[i+1][w+2]]))
def Tetromino_L6(lst):
    for i in range(n-1):
        for w in range(m-2):
            result.append(sum([lst[i][w],lst[i+1][w],lst[i+1][w+1],lst[i+1][w+2]]))
def Tetromino_L7(lst):
    for i in range(n-1):
        for w in range(m-2):
            result.append(sum([lst[i][w],lst[i][w+1],lst[i][w+2],lst[i+1][w]]))
def Tetromino_L8(lst):
    for i in range(n-1):
        for w in range(m-2):
            result.append(sum([lst[i][w],lst[i][w+1],lst[i][w+2],lst[i+1][w+2]]))

def Tetromino_Z1(lst):
    for i in range(n-2):
        for w in range(m-1):
            result.append(sum([lst[i][w],lst[i+1][w],lst[i+1][w+1],lst[i+2][w+1]]))
def Tetromino_Z2(lst):
    for i in range(n-2):
        for w in range(m-1):
            result.append(sum([lst[i][w+1],lst[i+1][w],lst[i+1][w+1],lst[i+2][w]]))
def Tetromino_Z3(lst):
    for i in range(n-1):
        for w in range(m-2):
            result.append(sum([lst[i+1][w],lst[i+1][w+1],lst[i][w+1],lst[i][w+2]]))
def Tetromino_Z4(lst):
    for i in range(n-1):
        for w in range(m-2):
            result.append(sum([lst[i][w],lst[i+1][w+1],lst[i][w+1],lst[i+1][w+2]]))
def Tetromino_T1(lst):
    for i in range(n-2):
        for w in range(m-1):
            result.append(sum([lst[i][w+1],lst[i+1][w],lst[i+1][w+1],lst[i+2][w+1]]))
def Tetromino_T2(lst):
    for i in range(n-2):
        for w in range(m-1):
            result.append(sum([lst[i+1][w+1],lst[i][w],lst[i+1][w],lst[i+2][w]]))
def Tetromino_T3(lst):
    for i in range(n-1):
        for w in range(m-2):
            result.append(sum([lst[i+1][w],lst[i+1][w+1],lst[i+1][w+2],lst[i][w+1]]))
def Tetromino_T4(lst):
    for i in range(n-1):
        for w in range(m-2):
            result.append(sum([lst[i][w],lst[i][w+1],lst[i][w+2],lst[i+1][w+1]]))

Tetromino_rectangle_1(lst)
Tetromino_rectangle_2(lst)
Tetromino_square(lst)
Tetromino_L1(lst)
Tetromino_L2(lst)
Tetromino_L3(lst)
Tetromino_L4(lst)
Tetromino_L5(lst)
Tetromino_L6(lst)
Tetromino_L7(lst)
Tetromino_L8(lst)
Tetromino_Z1(lst)
Tetromino_Z2(lst)
Tetromino_Z3(lst)
Tetromino_Z4(lst)
Tetromino_T1(lst)
Tetromino_T2(lst)
Tetromino_T3(lst)
Tetromino_T4(lst)

print(max(result))