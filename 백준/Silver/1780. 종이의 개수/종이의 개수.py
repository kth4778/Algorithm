import sys 
input = sys.stdin.readline

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
answer = [0,0,0]

def solution(y,x,size):
    global answer
    set_num = paper[y][x]

    for i in range(y, y + size):
        for j in range(x, x + size):
            if set_num != paper[i][j]:
                for q in range(3):
                    for w in range(3):
                        new_size = size // 3
                        solution(y + new_size * q, x + new_size * w,new_size)
                return
    
    else:
        answer[set_num + 1] += 1

solution(0,0,N)

for i in answer:
    print(i) 