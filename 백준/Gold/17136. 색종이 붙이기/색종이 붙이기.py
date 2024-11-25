import sys
input = sys.stdin.readline

def is_true(y1,x1,y2,x2):
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            if not paper[i][j]:
                return False
    
    return True

def attach(y1, x1, y2, x2, sticker):
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            paper[i][j] = sticker

def solution(p):
    global result

    for i in range(10):
        for j in range(10):
            if paper[i][j]:
                for q in range(5):
                    ny, nx = i + q, j + q                    
                    if count[q] and ny < 10  and nx < 10:
                        if is_true(i,j,ny,nx):
                            attach(i, j, ny, nx,0)
                            count[q] -= 1
                            solution(p + 1)
                            attach(i, j, ny ,nx, 1)
                            count[q] += 1
                return
    result = min(result, p)

paper = [list(map(int,input().split())) for _ in range(10)]
count = [5,5,5,5,5]
result = 26
solution(0)

if result == 26:
    print(-1)
else:
    print(result)